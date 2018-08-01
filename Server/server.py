from app import create_app

from config.config import DevConfig, ProductionConfig

if __name__ == '__main__':
    app = create_app(DevConfig)

    app.run(**app.config['RUN_SETTING'])
