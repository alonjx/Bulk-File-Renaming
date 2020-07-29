from pathlib import Path
import unittest
import random
import uuid
import shutil
import subprocess
import re
import sys

TMP_PATH = Path("tmp/")
FILE_TYPES = ['.json', '.txt', '.html', '.ini', '.jpg']


def build_directory_tree(parent_path, levels):
    if levels == 0:
        return

    # Create new level
    for i in range(random.randint(3, 6)):

        path = parent_path / uuid.uuid1().hex[:8]
        path.mkdir()
        if random.randint(1, 4) == 1:
            build_directory_tree(path, levels-1)
        else:
            t = uuid.uuid1().hex[:8]
            p = (parent_path / t).with_suffix(FILE_TYPES[random.randint(0, len(FILE_TYPES)-1)])
            p.touch()


class TestBulkFileRenaming(unittest.TestCase):
    def setUp(self):
        TMP_PATH.mkdir()
        tree_levels = random.randint(3, 5)
        build_directory_tree(TMP_PATH, tree_levels)

    def tearDown(self):
        shutil.rmtree(TMP_PATH)

    def test_rename_only(self):
        cmd = '%s Bulk-File-Renaming.py -r -n Batman -p "*.json" ./tmp' % sys.executable
        subprocess.call(cmd, shell=True)

        for f in TMP_PATH.glob('**/*.json'):
            assert re.match('Batman-\d+', f.stem), 'File name %s dosent matching the pattern "new-name-\d+"' % f

    def test_move_only(self):
        moveto_path = TMP_PATH / "moveto"
        moveto_path.mkdir()
        cmd = '%s Bulk-File-Renaming.py -d %s -r -p "*.txt" ./tmp' % (sys.executable, moveto_path)
        subprocess.call(cmd, shell=True)
        for f in TMP_PATH.glob("**/*.txt"):
            assert f.parent == moveto_path, 'file %s is not located where it should be' % f

        shutil.rmtree(moveto_path)

    def test_move_and_rename(self):
        moveto_path = TMP_PATH / "moveto"
        moveto_path.mkdir()
        new_name = 'Batman'
        cmd = '%s Bulk-File-Renaming.py -d %s -n %s -r -p "*.jpg" ./tmp' % (sys.executable, moveto_path, new_name)
        subprocess.call(cmd, shell=True)
        for f in TMP_PATH.glob("**/*.jpg"):
            assert f.parent == moveto_path, 'file %s is not located where it should be' % f
            assert re.match('Batman-\d+',f.stem), 'file % name is not matching the pattern' % f

        shutil.rmtree(moveto_path)

if __name__ == "__main__":
    unittest.main()
