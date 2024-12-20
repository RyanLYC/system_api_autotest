from common.tools import get_project_path, sep
from common.upload_img import upload_img


class TestUploadImg:
    def test_upload_img(self, token):
        img_path = get_project_path() + sep(["img", "station", "1.jpeg"], add_sep_before=True)
        upload_img(img_path, token('lyc'))
