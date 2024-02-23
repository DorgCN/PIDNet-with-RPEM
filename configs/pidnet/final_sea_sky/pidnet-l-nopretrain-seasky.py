_base_ = './pidnet-s-nopretrain-seasky.py'
# checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/pidnet/pidnet-l_imagenet1k_20230306-67889109.pth'  # noqa
model = dict(
    backbone=dict(
        channels=32,
        ppm_channels=112,
        num_stem_blocks=3,
        num_branch_blocks=5,
        # init_cfg=dict(checkpoint=checkpoint_file)
        ),
    decode_head=dict(in_channels=512, channels=512))
