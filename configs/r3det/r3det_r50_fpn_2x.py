_base_ = [
    '../_base_/models/r3det_r50_fpn.py',
    '../_base_/datasets/dotav1_rotational_detection.py',
    '../_base_/default_runtime.py'
]
# optimizer
optimizer = dict(type='SGD',
                 lr=4e-3,
                 momentum=0.9,
                 weight_decay=0.0001,
                 )  # paramwise_options=dict(bias_lr_mult=2, bias_decay_mult=0))
optimizer_config = dict(grad_clip=dict(max_norm=10, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=5000,
    warmup_ratio=0.1,
    step=[12, 16, 20])
total_epochs = 24

evaluation = dict(interval=1, metric='mAP')
