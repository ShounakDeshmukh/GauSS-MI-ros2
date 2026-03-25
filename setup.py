from setuptools import setup

package_name = 'gs_mapping'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YuhanXie',
    maintainer_email='yuhanxie@connect.hku.hk',
    description='The gs_mapping package',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gs_map = scripts.gs_map:main',
            'active_manage = scripts.active_recon.active_manage:main',
        ],
    },
)