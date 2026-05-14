from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class UploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.upload_image_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        self.upload_image_text = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        self.upload_image_description = page.get_by_test_id(f'{identifier}-image-upload-widget-info-description-text')
        self.upload_image_button = page.get_by_test_id(f'{identifier}-image-upload-widget-input')

        self.image_preview = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

    def upload_preview_image(self):
        self.upload_image_button.set_input_files('./testdata/files/image.png')

    def check_visible_upload_widget(self, title: str, description: str, is_image_uploaded=False):
        expect(self.upload_image_icon).to_be_visible()

        expect(self.upload_image_text).to_be_visible()
        expect(self.upload_image_text).to_have_text(title)

        expect(self.upload_image_description).to_be_visible()
        expect(self.upload_image_description).to_have_text(description)

        expect(self.upload_image_button).to_be_visible()
        expect(self.upload_image_button).to_be_enabled()

        if is_image_uploaded:
            expect(self.image_preview).to_be_visible()


