_base_ = ['./deeplabv3_r50-d8_4xb2-80k_cityscapes-512x1024.py', '../_base_/datasets/my_city.py']
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18),
    decode_head=dict(
        in_channels=512,
        channels=128,
        num_classes=7,
    ),
    auxiliary_head=dict(in_channels=256, channels=64, num_classes=7))
