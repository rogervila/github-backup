import argparse


class Console:
    parser = argparse.ArgumentParser(description='Backup your GitHub Repositories and Gists.')
    args = []

    def run(self):
        self.parser.add_argument('-t', '--token', required=True, metavar='<GITHUB_TOKEN>', type=str,
                                 help='Add your GitHub Token')
        self.args = self.parser.parse_args()
