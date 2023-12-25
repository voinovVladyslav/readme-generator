from options import Options


class Menu:
    def prompt_options(self) -> None:
        self.project_name = input('Project name:')
        print('Enter (y)es or (n)o if using next technologies:')
        self.celery = self._handle_input('celery:')
        self.storage = self._handle_input('storage:')
        self.pytest = self._handle_input('pytest:')

    def _handle_input(self, message: str) -> bool:
        while True:
            res = input(message).lower()
            if 'y' in res:
                return True
            if 'n' in res or not res:
                return False


    def get_options(self) -> Options:
        return Options(
            project_name=self.project_name,
            celery=self.celery,
            storage=self.storage,
            pytest=self.pytest,
        )
