# 工厂方法模式 允许接口创建对象, 但使用哪个类来创建对象，则是交由子类决定

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describle(self):
        pass


class PersonalSection(Section):
    def describle(self):
        print("Personal Section")


class AlbumSection(Section):
    def describle(self):
        print("Album Section")


class PatenSection(Section):
    def describle(self):
        print("Patent Section")


class PublicationSection(Section):
    def describle(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatenSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input()
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
