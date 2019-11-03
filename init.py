from rasa.nlu import config
from rasa.nlu.model import Trainer
from rasa.nlu.training_data import load_data


def train_nlu():
    training_data = load_data('data/data.json')
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")
    return model_directory

if __name__ ==  '__main__':
    train_nlu()