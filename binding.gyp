{
  'target_defaults': {
    'default_configuration': 'Release'
  },
  'targets': [
    {
      'target_name': 'saliency',
      'type': 'executable',
      'sources': [
        'saliency.cpp',
        'Saliency/GMRsaliency.cpp',
        'SLIC/SLIC.cpp'
      ],
      'libraries': [
        '<!@(pkg-config --libs opencv)'
      ],
      'ldflags': [
        '<!@(pkg-config --libs opencv)',
      ],
      'include_dirs': [
        '<!@(pkg-config opencv --cflags-only-I | sed s/-I//g)'
      ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
	      "CLANG_CXX_LANGUAGE_STANDARD": 'c++11',
              "MACOSX_DEPLOYMENT_TARGET":"10.9",
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '-O3',
              '<!@(pkg-config --libs-only-l opencv)',
            ],
            'OTHER_CPLUSPLUSFLAGS': [
              '-g',
              '-O3',
            ],

          }
        }]
      ]
    }
  ]
}
