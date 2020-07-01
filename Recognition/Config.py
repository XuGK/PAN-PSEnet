from dataclasses import dataclass, replace, field
from typing import List


@dataclass
class HP:

    #re: Resources
    
    experiment_name: str
    exp_dir: str
    train_data: str
    valid_data: str
    #langs: List[str]
    #pli: List[int]
    #mode: List[str]
    #task_id: List[int]
    save_path: str = field(init=False)
    select_data: List[int] = field(default_factory=list, init=False)
    batch_ratio: List[int] = field(default_factory=list, init=False)

    #hp: HP
    print_iter: int = 2
    character: dict = None
    shared_model: str = ''
    spath: str = ''
    Transformation: str = 'None'
    FeatureExtraction: str = 'VGG'
    SequenceModeling: str = 'BiLSTM'
    Prediction: str = 'CTC'
    share: str = 'CNN+LSTM'
    manualSeed: int = 1111
    workers: int = 4
    batch_size: int = 192
    num_iter: int = 300000
    valInterval: int = 1000
    saved_model: str = ''
    FT: bool = False
    adam: bool = False
    total_data_usage_ratio: str = '1.0'
    lr: float = 1.0
    beta1: float = 0.9
    rho: float = 0.95
    eps: float = 1e-8
    grad_clip: int = 5
    batch_max_length: int = 30
    imgH: int = 32
    imgW: int = 100
    rgb: bool = False
    sensitive: bool = False
    PAD: bool = False
    data_filtering_off: bool = False
    num_fiducial: int = 20
    input_channel: int = 1
    output_channel: int = 512
    hidden_size: int = 256

    def __post_init__(self):
        self.save_path = f'{self.exp_dir}/{self.experiment_name}'
        self.select_data = ['Syn','Real']
        self.batch_ratio = [0.5,0.5]


@dataclass
class langConfig:
    lang_name: str
    base_path: str
    useReal: bool
    useSyn: bool
    which_real_data: str = 'Real'
    which_syn_data: str = 'Syn'
    real_percent: float = 0.2
    syn_percent: float = 0.8


@dataclass
class taskConfig:
    task_name: str
    schedule: dict
    langs: List[langConfig] 
    hp: HP

hin_config = langConfig(lang_name='hin',base_path='/',useReal=True,useSyn=True)
ban_config = langConfig(lang_name='ban',base_path='/',useReal=True,useSyn=True)
hp_config = HP(experiment_name='test_loaders_single',exp_dir='exps',train_data='training',valid_data='validation',num_iter=10,valInterval=5)

task = taskConfig(task_name='hin_ban',langs=[hin_config,ban_config],schedule=[('ban',1),('hin',1)],hp=hp_config)
task_1 = taskConfig(task_name='hin',langs=[hin_config],schedule=[('hin',1)],hp=hp_config)    

#path = '/path/to/data/'
#test_new_train = Config(experiment_name='test_new_train_hin',exp_dir='tests',train_data=path+'training',valid_data=path+'validation')
#/taskconfig_hin = Task(lang='hin',numiters=10)