import unittest
import subprocess
import json
from pathlib import Path
import shutil

class TerraformTestCase(unittest.TestCase):
    def setUp(self,):
        subprocess.run(["terraform","init"])

    def tearDown(self,):
        ## Clear up the various terraform state and caches
        Path('terraform.tfstate').unlink(missing_ok=True)
        Path('terraform.tfstate.backup').unlink(missing_ok=True)
        Path('.terraform.lock.hcl').unlink(missing_ok=True)
        shutil.rmtree(".terraform/", ignore_errors=True)

    def do_test_with_value(self,value):
        subprocess.run(["terraform","apply","-auto-approve","-var", f"url={value}"])
        proc = subprocess.run(
            ["terraform","output","-json"],
             stdout=subprocess.PIPE
        )
        datastr = str(proc.stdout,'utf8')
        try:
            return json.loads(datastr)
        except json.decoder.JSONDecodeError:
            print (f"JSONDecode failed: {datastr!r}")
            raise


    @unittest.expectedFailure
    def test_full_url_with_withspace(self,):
        result = self.do_test_with_value(
            "http://www.google.com  "
        )
        self.assertEqual(result['scheme']['value'],'http')
        self.assertEqual(result['netloc']['value'],'www.google.com')

    def test_full_url_with_newline(self,):
        result = self.do_test_with_value(
            "http://www.google.com\n"
        )
        self.assertEqual(result['scheme']['value'],'http')
        self.assertEqual(result['netloc']['value'],'www.google.com')
 
    def test_full_url(self,):
        result = self.do_test_with_value(
            "http://user:pass@www.example.com:8080/path?query1=1&query2=2#frag"
        )
        self.assertEqual(result['scheme']['value'],'http')
        self.assertEqual(result['username']['value'],'user')
        self.assertEqual(result['password']['value'],'pass')
        self.assertEqual(result['password']['sensitive'],True)
        self.assertEqual(result['hostname']['value'],'www.example.com')
        self.assertEqual(result['port']['value'],'8080')
        self.assertEqual(result['path']['value'],'/path')
        self.assertEqual(result['query']['value'],'query1=1&query2=2')
        self.assertEqual(result['fragment']['value'],'frag')

if __name__ == "__main__":
    unittest.main()
