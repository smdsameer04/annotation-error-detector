def extract_features(box):
    x, y, w, h = box

    area = w * h
    aspect_ratio = w / (h + 1)
    center_x = x + w / 2
    center_y = y + h / 2

    return [area, aspect_ratio, center_x, center_y]