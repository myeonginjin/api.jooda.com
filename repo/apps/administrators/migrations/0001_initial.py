# Generated by Django 4.1.7 on 2023-04-11 02:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Administrator",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="관리자 계정 pk",
                    ),
                ),
                (
                    "login_id",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        unique=True,
                        verbose_name="로그인 id",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True, default="", max_length=70, verbose_name="로그인 비밀번호"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="전화번호"
                    ),
                ),
                (
                    "autorization_token",
                    models.CharField(
                        blank=True, max_length=70, null=True, verbose_name="인증 토큰"
                    ),
                ),
            ],
            options={
                "verbose_name": "3.1 교회 관리자 기본 정보",
                "verbose_name_plural": "3.1 교회 관리자 기본 정보",
            },
        ),
    ]