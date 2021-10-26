_base_ = [
     '../../_base_/datasets/ade20k.py',
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_80k.py'
]


find_unused_parameters=True
weight=10.0
tau=1.0
distiller = dict(
    type='SegmentationDistiller',
    teacher_pretrained = 'pretraind_model/pspnet_r101-d8_512x512_160k_ade20k_20200615_100650-967c316f.pth',
    distill_cfg = [ dict(student_module = 'decode_head.conv_seg',
                         teacher_module = 'decode_head.conv_seg',
                         output_hook = True,
                         methods=[dict(type='ChannelWiseDivergence',
                                       name='loss_cwd',
                                       student_channels = 150,
                                       teacher_channels = 150,
                                       tau = tau,
                                       weight =weight,
                                       )
                                ]
                        ),
                    
                   ]
    )

student_cfg = 'configs/pspnet/pspnet_r18-d8_512x512_80k_ade20k.py'
teacher_cfg = 'configs/pspnet/pspnet_r101-d8_512x512_160k_ade20k.py'

