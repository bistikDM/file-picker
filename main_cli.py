import os
import shutil
from pathlib import Path

import build
import copy
import setup
import test_env


def cherry_pick(file_name: str):
    # TODO: Allow user to pick a certain option from a section to copy.
    pass


def print_storage():
    # TODO: display the tree of the "image repo" and its content.
    pass


def main():
    # TESTING
    test_env.create_test_storage_environment()
    configuration_file = setup.get_config()
    print("Configuration file:", configuration_file)
    while True:
        print("***TEST MENU***")
        print("\t1). Select a build.")
        print("\t2). Remove a build.")
        print("\t3). Add a build.")
        print("\t4). Edit a build.")
        print("\t5). Cherry-pick from build (Not implemented yet).")
        print("\t6). Add new files (Not implemented yet).")
        # Will try to associate files to build options and print
        # what's not being used as well as what files are missing for a build.
        print("\t7). Print report (Not implemented yet).")
        print("\t8). Print verbose tree structure (Not implemented yet).")
        print("\t9). Reset test environment.")
        print("\t0). Exit.")
        try:
            selection = input("Enter a number: ")
            if selection == "1":
                selected_build = build.select_build(configuration_file)
                if build:
                    files = build.build_paths(configuration_file, selected_build)
                    destination = str(os.path.join(setup.project_root, "test-destination"))
                    if not Path(destination).exists():
                        os.makedirs(destination)
                    print("Copying the following files to %s:" % destination)
                    for file in files:
                        print("\t %s" % file[1])
                    copy.copy_files(files, destination)
            elif selection == "2":
                build.remove_build(configuration_file)
            elif selection == "3":
                build.add_new_build(configuration_file)
            elif selection == "4":
                build.edit_build(configuration_file)
            elif selection == "9":
                shutil.rmtree(setup.project_root)
                shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev1"))
                shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev2"))
                shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev3"))
                test_env.create_test_storage_environment()
                configuration_file = setup.get_config()
            elif selection == "0":
                break
            else:
                pass
        except ValueError:
            pass
    shutil.rmtree(setup.project_root)
    shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev1"))
    shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev2"))
    shutil.rmtree(os.path.join(os.path.abspath(os.sep), "file-picker-dev3"))


if __name__ == "__main__":
    main()