from options import Options


class Menu(Options):
    def __init__(self):
        self.options = {}

    def prompt_options(self) -> None:
        self.options['']

    def _handle_input(self, message: str) -> bool:
        while True:
            res = input(message).lower()
            if 'y' in res:
                return True
            elif 'n' in res:
                return False


    def get_options(self) -> dict:
        return {
            'project_name': self.project_name,
            'celery': self.celery,
            'storage': self.storage,
            'pytest': self.pytest,
        }
