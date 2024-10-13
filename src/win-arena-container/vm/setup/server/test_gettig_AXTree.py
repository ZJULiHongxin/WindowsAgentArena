from pywinauto import Desktop
from pywinauto.base_wrapper import BaseWrapper
import lxml.etree
from flask import Flask, request, jsonify, send_file, abort  # , send_from_directory
from tqdm import tqdm
from main import _accessibility_ns_map, _create_pywinauto_node

desktop: Desktop = Desktop(backend='uia')

xml_node = lxml.etree.Element("desktop", nsmap=_accessibility_ns_map)

windows = desktop.windows()
for wnd in tqdm(windows, total=len(windows)):
    print("Win UIA AT parsing: %s(%d)", wnd.element_info.name, len(wnd.children()))
    node = _create_pywinauto_node(wnd, 1)
    xml_node.append(node)


result = jsonify({"AT": lxml.etree.tostring(xml_node, encoding="unicode")})