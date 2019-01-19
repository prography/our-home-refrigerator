import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--user_info_dir', type=str, default='userInfo', help='location of database for user information')
parser.add_argument('--user_info_db', type=str, default='userInfo.db', help='name of database for user information')
parser.add_argument('--ip_name', type=str, default='ip')
parser.add_argument('--user_id_name', type=str, default='user_id')
parser.add_argument('--respond_name', type=str, default='res')


def get_config():
    return parser.parse_args()
