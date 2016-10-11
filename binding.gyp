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
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '-g',
              '-mmacosx-version-min=10.7',
              '-O3',
              '-Wall'
            ],
            'OTHER_CPLUSPLUSFLAGS': [
              '-g',
              '-mmacosx-version-min=10.7',
              '-std=c++11',
              '-stdlib=libc++',
              '-stdlib=libstdc++',
              '-O3',
              '-Wall'
            ],

          }
        }]
      ]
    }
  ]
}
