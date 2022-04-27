import xmltodict
xml_data = """
    <metadata>
<variables.beauty_analytical_bjic_glic_mbc_sgic>false</variables.beauty_analytical_bjic_glic_mbc_sgic>
<variables.role_lab_analyst>false</variables.role_lab_analyst>
<variables.xbu_analytical_analytical_bjic_gic_laic_sgic_whbc>false</variables.xbu_analytical_analytical_bjic_gic_laic_sgic_whbc>
<variables.babyfem_sensory_sensory_bjic_gic_laic_whbc>false</variables.babyfem_sensory_sensory_bjic_gic_laic_whbc>
<variables.corpfunct_tpt_gladjv_kpic>false</variables.corpfunct_tpt_gladjv_kpic>
<variables.application_access_for>Nexus</variables.application_access_for>
<variables.babydem_analytical_analytical_bjic_gic_gpdf_laic_sgic_whbc>false</variables.babydem_analytical_analytical_bjic_gic_gpdf_laic_sgic_whbc>
<variables.health_analytical_analytical_bjic_gic_glic_mbc>false</variables.health_analytical_analytical_bjic_gic_glic_mbc>
<variables.corpfunct_tpt_materialscience_brtc_tsdc>false</variables.corpfunct_tpt_materialscience_brtc_tsdc>
<variables.role_rd_stability_coordinator>false</variables.role_rd_stability_coordinator>
</metadata>
"""

d = xmltodict.parse(xml_data)
print(d['metadata']['variables.beauty_analytical_bjic_glic_mbc_sgic'])
with open(r'C:\Users\prakh\Desktop\abc.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
d1= xmltodict.parse(my_xml)
print(d1['metadata']['variables.beauty_analytical_bjic_glic_mbc_sgic'])