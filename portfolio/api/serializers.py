from django.db.models.expressions import fields
from rest_framework import serializers

from .models import Project, ProjectImage, Tag, Timeline


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = [
            "id",
            "year",
            "milestone",
            "duration",
            "details",
        ]

    def create(self, validated_data):
        timeline = Timeline.objects.create(**validated_data)

        return timeline

    def update(self, instance, validated_data):
        instance.year = validated_data.get("year", instance.year)
        instance.milestone = validated_data.get("milestone", instance.milestone)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.details = validated_data.get("details", instance.details)
        instance.save()

        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "project"]


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tags",
            "live_url",
            "source_url",
            "images",
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        project = Project.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            project.tags.add(tag)

        return project

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags")
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.live_url = validated_data.get("live_url", instance.live_url)
        instance.source_url = validated_data.get("source_url", instance.source_url)
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        return instance
