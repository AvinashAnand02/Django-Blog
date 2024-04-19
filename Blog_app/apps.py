from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog_app'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
