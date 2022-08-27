def create_folder(path):
    # checking for folder existence
    if not os.path.exists(path):
        # print(path)
        # create folder
        os.mkdir(path)


def create_empty_file(path):
    open(path, 'a').close()


def remote(path):
    # check
    if os.path.exists(path):
        if '.' in path:
            if os.path.exists(path):
                # remote
                print('asdf')
                os.remove(path)
        elif len(os.listdir(path)) == 0:
            os.rmdir(path)
        elif len(os.listdir(path)) != 0:
            shutil.rmtree(path)


def copy(path):
    if not os.path.exists(path):
        # если существует path то не копируем
        if '.' in path:
            shutil.copy(path, path + '_copy')
        else:
            shutil.copytree(path, path + '_copy')


def view(*args):
    question = input ('Save listdir in file? y/all keys')
    if not args:
        if question == 'y':
            with ('listdir.txt', 'w') as f:
                f.write(os.listdir().reverse())
        return os.listdir()
    else:
        if question == 'y':
            with ('listdir.txt', 'w') as f:
                f.write(os.listdir(*args).reverse())
        return os.listdir(*args)


def view_folders(*args):
    if args:
        return list(filter(lambda x: '.' not in x, os.listdir(*args)))
    else:
        return list(filter(lambda x: '.' not in x, os.listdir()))


def view_files(*args):
    if args:
        return list(filter(lambda x: '.' in x, os.listdir(*args)))
    else:
        return list(filter(lambda x: '.' in x, os.listdir()))


def system_information():
    return str('My OS is, {}, ({})'.format(sys.platform, os.name))


def creator():
    print('****MIKHAIL****')