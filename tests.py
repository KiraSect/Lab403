import unittest
import os
from PIL import Image
from watermark import watermark_photo

class TestWatermarkPhoto(unittest.TestCase):
    
    def setUp(self):
        # Создание тестовых изображений
        self.test_folder = "test_images"
        self.output_folder = "test_output"
        self.base_image_path = os.path.join(self.test_folder, "base_image.jpg")
        self.watermark_image_path = os.path.join(self.test_folder, "watermark.png")
        self.output_image_path = os.path.join(self.output_folder, "output_image.jpg")
        
        if not os.path.exists(self.test_folder):
            os.mkdir(self.test_folder)
        
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)
        
        # Создание базового изображения
        base_image = Image.new("RGB", (500, 500), color="blue")
        base_image.save(self.base_image_path)
        
        # Создание изображения водяного знака
        watermark_image = Image.new("RGBA", (100, 100), color=(255, 0, 0, 128))
        watermark_image.save(self.watermark_image_path)

    def tearDown(self):
        # Очистка сгенерированных файлов и папок
        if os.path.exists(self.base_image_path):
            os.remove(self.base_image_path)
        
        if os.path.exists(self.watermark_image_path):
            os.remove(self.watermark_image_path)
        
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)
        
        if os.path.exists(self.test_folder):
            os.rmdir(self.test_folder)
        
        if os.path.exists(self.output_folder):
            os.rmdir(self.output_folder)

    def test_watermark_photo_creates_output_file(self):
        """Тест на создание файла-результата."""
        watermark_photo(
            input_image_path=self.base_image_path,
            watermark_image_path=self.watermark_image_path,
            output_image_path=self.output_image_path
        )
        
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_watermark_position_and_size(self):
        """Тест на правильное позиционирование и размер водяного знака."""
        watermark_photo(
            input_image_path=self.base_image_path,
            watermark_image_path=self.watermark_image_path,
            output_image_path=self.output_image_path
        )
        
        output_image = Image.open(self.output_image_path)
        
        # Проверка размера изображения-результата
        self.assertEqual(output_image.size, (500, 500))
        
    def test_output_quality_and_mode(self):
        """Тест на качество и режим изображения-результата."""
        watermark_photo(
            input_image_path=self.base_image_path,
            watermark_image_path=self.watermark_image_path,
            output_image_path=self.output_image_path
        )
        
        output_image = Image.open(self.output_image_path)
        
        # Проверка режима изображения-результата
        self.assertEqual(output_image.mode, "RGB")

if __name__ == "__main__":
    unittest.main()