import os
from xml.etree import ElementTree


def _get_children_by_attr(xml_path, tag, attr, value):
    vals = []
    tree = ElementTree.parse(xml_path)
    for elem in tree.findall(tag):
        val = elem.get(attr)
        if val == value:
            for c in elem.getchildren():
                vals.append(c.text)
    return vals


def _get_value_by_tag(xml_path, tag):
    vals = []
    tree = ElementTree.parse(xml_path)
    for elem in tree.findall(tag):
        vals.append(elem.text)
    return vals


class Xml:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls._instance = Xml()
        return cls._instance

    @staticmethod
    def get_value_by_tag(xml_path, tag):
        return _get_value_by_tag(xml_path, tag)

    @staticmethod
    def get_children_by_attr(xml_path, tag, attr, value):
        return _get_children_by_attr(xml_path, tag, attr, value)


if __name__ == "__main__":
    print(Xml.get_children_by_attr(os.path.join(os.getcwd(), "config", "api.xml"), "url", "name", "login"))
