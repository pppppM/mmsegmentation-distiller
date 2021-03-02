_base_ = [
     '../../_base_/datasets/cityscapes.py',
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_80k.py'
]


find_unused_parameters=True
weight=5.0
tau=1.0
distiller = dict(
    type='SegmentationDistiller',
    teacher_pretrained = 'pretrained_model/pspnet_r101b-d8_512x1024_80k_cityscapes_20201226_170012-3a4d38ab.pth',
    distill_cfg = [ dict(student_module = 'decode_head.conv_seg',
                         teacher_module = 'decode_head.conv_seg',
                         output_hook = True,
                         methods=[dict(type='ChannelWiseDivergence',
                                       name='loss_cwd',
                                       student_channels = 19,
                                       teacher_channels = 19,
                                       tau = tau,
                                       weight =weight,
                                       )
                                ]
                        ),
                    
                   ]
    )

student_cfg = 'configs/pspnet/pspnet_r18-d8_512x1024_80k_cityscapes.py'
teacher_cfg = 'configs/pspnet/pspnet_r101-d8_512x1024_80k_cityscapes.py'