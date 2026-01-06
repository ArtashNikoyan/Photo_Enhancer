import cv2
import numpy as np
import tensorflow as tf

PATCH_SIZE = 224
PATCH_STRIDE = PATCH_SIZE // 2


def extract_patches(img, patch_size=224, step=112):
    H, W, C = img.shape
    patches, positions = [], []

    y_poss = list(range(0, H - patch_size + 1, step))
    if y_poss[-1] + patch_size < H:
        y_poss.append(H - patch_size)

    x_poss = list(range(0, W - patch_size + 1, step))
    if x_poss[-1] + patch_size < W:
        x_poss.append(W - patch_size)

    for y in y_poss:
        for x in x_poss:
            patches.append(img[y:y+patch_size, x:x+patch_size])
            positions.append((y, x))

    return np.array(patches), positions, H, W


def get_weight_map(patch_size, eps=0.05):
    w = np.hanning(patch_size)
    w = np.maximum(w, eps)
    return np.outer(w, w)[..., None]


def merge_patches(patches, positions, H, W, patch_size):
    C = patches[0].shape[2]
    output = np.zeros((H, W, C), np.float32)
    weight = np.zeros((H, W, 1), np.float32)

    weight_map = get_weight_map(patch_size)

    for patch, (y, x) in zip(patches, positions):
        output[y:y+patch_size, x:x+patch_size] += patch * weight_map
        weight[y:y+patch_size, x:x+patch_size] += weight_map

    output /= np.maximum(weight, 1e-6)
    return np.clip(output, 0, 255).astype(np.uint8)


def pad_to_square(img, patch_size):
    h, w, _ = img.shape
    side = max(h, w)
    target = ((side + patch_size - 1) // patch_size) * patch_size

    pad_h = target - h
    pad_w = target - w

    top, bottom = pad_h // 2, pad_h - pad_h // 2
    left, right = pad_w // 2, pad_w - pad_w // 2

    padded = np.pad(
        img,
        ((top, bottom), (left, right), (0, 0)),
        mode="reflect"
    )

    return padded, (top, left, h, w)


def unpad(img, pad):
    top, left, h, w = pad
    return img[top:top+h, left:left+w]


def predict_img(model, img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img, pad = pad_to_square(img, PATCH_SIZE)
    patches, pos, H, W = extract_patches(img, PATCH_SIZE, PATCH_STRIDE)

    X = patches.astype(np.float32) / 127.5 - 1.0
    preds = model.predict(X, verbose=0)

    preds = ((preds + 1.0) * 127.5).astype(np.uint8)
    out = merge_patches(preds, pos, H, W, PATCH_SIZE)

    return unpad(out, pad)
