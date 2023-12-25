class ReadmeGenerator:
    def __init__(
        self,
        project_name: str,
        celery: bool = False,
        storage: bool = False,
        pytest: bool = False,
        https: bool = False,
    ):
        self.project_name = project_name
        self.celery = celery
        self.storage = storage
        self.pytest = pytest
        self.https = https

    def generate_content(self) -> str:
        res = self._generate_title()
        res += self._generate_local_setup()
        return res

    def _generate_title(self):
        return f'# {self.project_name}\n\n'

    def _generate_local_setup(self) -> str:
        res = '## Local Setup\n\n'
        res += self._copy_env()
        if self.storage:
            res += self._make_storage_bucket()
        res += self._build_project()
        res += self._create_superuser()
        return res

    def _copy_env(self) -> str:
        return (
            "Create .env file\n\n"
            f"{self._bash_command('cp .env.example .env')}"
        )

    def _make_storage_bucket(self) -> str:
        return (
            f'Run Storage\n\n'
            f'{self._bash_command("docker compose up storage")}'
            f'Go to {self._storage_url()}\n\n'
            f'Create Bucket\n\n'
            f'Fill variables in .env file\n\n'
            f'- AWS_STORAGE_BUCKET_NAME\n'
            f'- AWS_S3_ACCESS_KEY_ID\n'
            f'- AWS_S3_SECRET_ACCESS_KEY\n\n'
            f'More info can be found [here](https://s3ninja.net/).\n\n'
        )

    def _storage_url(self) -> str:
        url = "http://127.0.0.1:9000/ui"
        return f"[{url}]({url})"

    def _build_project(self) -> str:
        return (
            "Build Project\n\n"
            f"{self._bash_command('docker compose build')}"
        )

    @staticmethod
    def _bash_command(command: str) -> str:
        return (
            "```bash\n"
            f'{command}\n'
            "```\n\n"
        )

    def _run_project(self) -> str:
        return (
            'Run Project\n\n'
            f"{self._bash_command('docker compose up -d')}"
        )

    def _create_superuser(self) -> str:
        return (
            'Create superuser\n\n'
            'Inside Python container execute command\n\n'
            f'{self._bash_command("python manage.py createsuperuser")}'
            'Follow further instructions\n\n'
        )

    def _containers_table(self) -> str:
        return
