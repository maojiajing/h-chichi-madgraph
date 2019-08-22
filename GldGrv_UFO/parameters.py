# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Fri 26 Jul 2019 17:18:54



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
RRd1x1 = Parameter(name = 'RRd1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd1x1}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 1, 1 ])

RRd2x2 = Parameter(name = 'RRd2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd2x2}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 2, 2 ])

RRd3x3 = Parameter(name = 'RRd3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.938737896,
                   texname = '\\text{RRd3x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 3, 3 ])

RRd3x6 = Parameter(name = 'RRd3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.344631925,
                   texname = '\\text{RRd3x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 3, 6 ])

RRd4x4 = Parameter(name = 'RRd4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd4x4}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 4, 4 ])

RRd5x5 = Parameter(name = 'RRd5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd5x5}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 5, 5 ])

RRd6x3 = Parameter(name = 'RRd6x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.344631925,
                   texname = '\\text{RRd6x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 6, 3 ])

RRd6x6 = Parameter(name = 'RRd6x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.938737896,
                   texname = '\\text{RRd6x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 6, 6 ])

alp = Parameter(name = 'alp',
                nature = 'external',
                type = 'real',
                value = -0.11382521,
                texname = '\\alpha',
                lhablock = 'FRALPHA',
                lhacode = [ 1 ])

RMUH = Parameter(name = 'RMUH',
                 nature = 'external',
                 type = 'real',
                 value = 357.680977,
                 texname = '\\text{RMUH}',
                 lhablock = 'HMIX',
                 lhacode = [ 1 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 9.74862403,
               texname = 't_b',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MA2 = Parameter(name = 'MA2',
                nature = 'external',
                type = 'real',
                value = 166439.065,
                texname = '\\text{Subsuperscript}[m,A,2]',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

RmD21x1 = Parameter(name = 'RmD21x1',
                    nature = 'external',
                    type = 'real',
                    value = 273684.674,
                    texname = '\\text{RmD21x1}',
                    lhablock = 'MSD2',
                    lhacode = [ 1, 1 ])

RmD22x2 = Parameter(name = 'RmD22x2',
                    nature = 'external',
                    type = 'real',
                    value = 273684.674,
                    texname = '\\text{RmD22x2}',
                    lhablock = 'MSD2',
                    lhacode = [ 2, 2 ])

RmD23x3 = Parameter(name = 'RmD23x3',
                    nature = 'external',
                    type = 'real',
                    value = 270261.969,
                    texname = '\\text{RmD23x3}',
                    lhablock = 'MSD2',
                    lhacode = [ 3, 3 ])

RmE21x1 = Parameter(name = 'RmE21x1',
                    nature = 'external',
                    type = 'real',
                    value = 18630.6287,
                    texname = '\\text{RmE21x1}',
                    lhablock = 'MSE2',
                    lhacode = [ 1, 1 ])

RmE22x2 = Parameter(name = 'RmE22x2',
                    nature = 'external',
                    type = 'real',
                    value = 18630.6287,
                    texname = '\\text{RmE22x2}',
                    lhablock = 'MSE2',
                    lhacode = [ 2, 2 ])

RmE23x3 = Parameter(name = 'RmE23x3',
                    nature = 'external',
                    type = 'real',
                    value = 17967.6406,
                    texname = '\\text{RmE23x3}',
                    lhablock = 'MSE2',
                    lhacode = [ 3, 3 ])

RmL21x1 = Parameter(name = 'RmL21x1',
                    nature = 'external',
                    type = 'real',
                    value = 38155.67,
                    texname = '\\text{RmL21x1}',
                    lhablock = 'MSL2',
                    lhacode = [ 1, 1 ])

RmL22x2 = Parameter(name = 'RmL22x2',
                    nature = 'external',
                    type = 'real',
                    value = 38155.67,
                    texname = '\\text{RmL22x2}',
                    lhablock = 'MSL2',
                    lhacode = [ 2, 2 ])

RmL23x3 = Parameter(name = 'RmL23x3',
                    nature = 'external',
                    type = 'real',
                    value = 37828.6769,
                    texname = '\\text{RmL23x3}',
                    lhablock = 'MSL2',
                    lhacode = [ 3, 3 ])

RMx1 = Parameter(name = 'RMx1',
                 nature = 'external',
                 type = 'real',
                 value = 101.396534,
                 texname = '\\text{RMx1}',
                 lhablock = 'MSOFT',
                 lhacode = [ 1 ])

RMx2 = Parameter(name = 'RMx2',
                 nature = 'external',
                 type = 'real',
                 value = 191.504241,
                 texname = '\\text{RMx2}',
                 lhablock = 'MSOFT',
                 lhacode = [ 2 ])

RMx3 = Parameter(name = 'RMx3',
                 nature = 'external',
                 type = 'real',
                 value = 588.263031,
                 texname = '\\text{RMx3}',
                 lhablock = 'MSOFT',
                 lhacode = [ 3 ])

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = 32337.4943,
                 texname = '\\text{Subsuperscript}\\left[m,H_d,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = -128800.134,
                 texname = '\\text{Subsuperscript}\\left[m,H_u,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ21x1 = Parameter(name = 'RmQ21x1',
                    nature = 'external',
                    type = 'real',
                    value = 299836.701,
                    texname = '\\text{RmQ21x1}',
                    lhablock = 'MSQ2',
                    lhacode = [ 1, 1 ])

RmQ22x2 = Parameter(name = 'RmQ22x2',
                    nature = 'external',
                    type = 'real',
                    value = 299836.701,
                    texname = '\\text{RmQ22x2}',
                    lhablock = 'MSQ2',
                    lhacode = [ 2, 2 ])

RmQ23x3 = Parameter(name = 'RmQ23x3',
                    nature = 'external',
                    type = 'real',
                    value = 248765.367,
                    texname = '\\text{RmQ23x3}',
                    lhablock = 'MSQ2',
                    lhacode = [ 3, 3 ])

RmU21x1 = Parameter(name = 'RmU21x1',
                    nature = 'external',
                    type = 'real',
                    value = 280382.106,
                    texname = '\\text{RmU21x1}',
                    lhablock = 'MSU2',
                    lhacode = [ 1, 1 ])

RmU22x2 = Parameter(name = 'RmU22x2',
                    nature = 'external',
                    type = 'real',
                    value = 280382.106,
                    texname = '\\text{RmU22x2}',
                    lhablock = 'MSU2',
                    lhacode = [ 2, 2 ])

RmU23x3 = Parameter(name = 'RmU23x3',
                    nature = 'external',
                    type = 'real',
                    value = 179137.072,
                    texname = '\\text{RmU23x3}',
                    lhablock = 'MSU2',
                    lhacode = [ 3, 3 ])

RNN1x1 = Parameter(name = 'RNN1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.98636443,
                   texname = '\\text{RNN1x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 1 ])

RNN1x2 = Parameter(name = 'RNN1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.0531103553,
                   texname = '\\text{RNN1x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 2 ])

RNN1x3 = Parameter(name = 'RNN1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.146433995,
                   texname = '\\text{RNN1x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 3 ])

RNN1x4 = Parameter(name = 'RNN1x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.0531186117,
                   texname = '\\text{RNN1x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 4 ])

RNN2x1 = Parameter(name = 'RNN2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.0993505358,
                   texname = '\\text{RNN2x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 1 ])

RNN2x2 = Parameter(name = 'RNN2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.944949299,
                   texname = '\\text{RNN2x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 2 ])

RNN2x3 = Parameter(name = 'RNN2x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.26984672,
                   texname = '\\text{RNN2x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 3 ])

RNN2x4 = Parameter(name = 'RNN2x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.156150698,
                   texname = '\\text{RNN2x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 4 ])

RNN3x1 = Parameter(name = 'RNN3x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.0603388002,
                   texname = '\\text{RNN3x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 1 ])

RNN3x2 = Parameter(name = 'RNN3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.0877004854,
                   texname = '\\text{RNN3x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 2 ])

RNN3x3 = Parameter(name = 'RNN3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.695877493,
                   texname = '\\text{RNN3x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 3 ])

RNN3x4 = Parameter(name = 'RNN3x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.710226984,
                   texname = '\\text{RNN3x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 4 ])

RNN4x1 = Parameter(name = 'RNN4x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.116507132,
                   texname = '\\text{RNN4x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 1 ])

RNN4x2 = Parameter(name = 'RNN4x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.310739017,
                   texname = '\\text{RNN4x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 2 ])

RNN4x3 = Parameter(name = 'RNN4x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.64922596,
                   texname = '\\text{RNN4x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 3 ])

RNN4x4 = Parameter(name = 'RNN4x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.684377823,
                   texname = '\\text{RNN4x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 4 ])

RRl1x1 = Parameter(name = 'RRl1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl1x1}',
                   lhablock = 'SELMIX',
                   lhacode = [ 1, 1 ])

RRl2x2 = Parameter(name = 'RRl2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl2x2}',
                   lhablock = 'SELMIX',
                   lhacode = [ 2, 2 ])

RRl3x3 = Parameter(name = 'RRl3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.28248719,
                   texname = '\\text{RRl3x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 3, 3 ])

RRl3x6 = Parameter(name = 'RRl3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.959271071,
                   texname = '\\text{RRl3x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 3, 6 ])

RRl4x4 = Parameter(name = 'RRl4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl4x4}',
                   lhablock = 'SELMIX',
                   lhacode = [ 4, 4 ])

RRl5x5 = Parameter(name = 'RRl5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl5x5}',
                   lhablock = 'SELMIX',
                   lhacode = [ 5, 5 ])

RRl6x3 = Parameter(name = 'RRl6x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.959271071,
                   texname = '\\text{RRl6x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 3 ])

RRl6x6 = Parameter(name = 'RRl6x6',
                   nature = 'external',
                   type = 'real',
                   value = -0.28248719,
                   texname = '\\text{RRl6x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.934,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

MP = Parameter(name = 'MP',
               nature = 'external',
               type = 'real',
               value = 2.435323203596526e18,
               texname = 'M_P',
               lhablock = 'SMINPUTS',
               lhacode = [ 10 ])

MM32 = Parameter(name = 'MM32',
                 nature = 'external',
                 type = 'real',
                 value = 1.e-13,
                 texname = '\\text{MM32}',
                 lhablock = 'SMINPUTS',
                 lhacode = [ 11 ])

RRn1x1 = Parameter(name = 'RRn1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn1x1}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 1, 1 ])

RRn2x2 = Parameter(name = 'RRn2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn2x2}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 2, 2 ])

RRn3x3 = Parameter(name = 'RRn3x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn3x3}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 3, 3 ])

Rtd3x3 = Parameter(name = 'Rtd3x3',
                   nature = 'external',
                   type = 'real',
                   value = -110.693742,
                   texname = '\\text{Rtd3x3}',
                   lhablock = 'TD',
                   lhacode = [ 3, 3 ])

Rte3x3 = Parameter(name = 'Rte3x3',
                   nature = 'external',
                   type = 'real',
                   value = -25.4019727,
                   texname = '\\text{Rte3x3}',
                   lhablock = 'TE',
                   lhacode = [ 3, 3 ])

Rtu3x3 = Parameter(name = 'Rtu3x3',
                   nature = 'external',
                   type = 'real',
                   value = -444.752457,
                   texname = '\\text{Rtu3x3}',
                   lhablock = 'TU',
                   lhacode = [ 3, 3 ])

RUU1x1 = Parameter(name = 'RUU1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.916834859,
                   texname = '\\text{RUU1x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 1 ])

RUU1x2 = Parameter(name = 'RUU1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.399266629,
                   texname = '\\text{RUU1x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 2 ])

RUU2x1 = Parameter(name = 'RUU2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.399266629,
                   texname = '\\text{RUU2x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 1 ])

RUU2x2 = Parameter(name = 'RUU2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.916834859,
                   texname = '\\text{RUU2x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 2 ])

RMNS1x1 = Parameter(name = 'RMNS1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS1x1}',
                    lhablock = 'UPMNS',
                    lhacode = [ 1, 1 ])

RMNS2x2 = Parameter(name = 'RMNS2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS2x2}',
                    lhablock = 'UPMNS',
                    lhacode = [ 2, 2 ])

RMNS3x3 = Parameter(name = 'RMNS3x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS3x3}',
                    lhablock = 'UPMNS',
                    lhacode = [ 3, 3 ])

RRu1x1 = Parameter(name = 'RRu1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu1x1}',
                   lhablock = 'USQMIX',
                   lhacode = [ 1, 1 ])

RRu2x2 = Parameter(name = 'RRu2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu2x2}',
                   lhablock = 'USQMIX',
                   lhacode = [ 2, 2 ])

RRu3x3 = Parameter(name = 'RRu3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.55364496,
                   texname = '\\text{RRu3x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 3, 3 ])

RRu3x6 = Parameter(name = 'RRu3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.83275282,
                   texname = '\\text{RRu3x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 3, 6 ])

RRu4x4 = Parameter(name = 'RRu4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu4x4}',
                   lhablock = 'USQMIX',
                   lhacode = [ 4, 4 ])

RRu5x5 = Parameter(name = 'RRu5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu5x5}',
                   lhablock = 'USQMIX',
                   lhacode = [ 5, 5 ])

RRu6x3 = Parameter(name = 'RRu6x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.83275282,
                   texname = '\\text{RRu6x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 6, 3 ])

RRu6x6 = Parameter(name = 'RRu6x6',
                   nature = 'external',
                   type = 'real',
                   value = -0.55364496,
                   texname = '\\text{RRu6x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 6, 6 ])

RCKM1x1 = Parameter(name = 'RCKM1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM1x1}',
                    lhablock = 'VCKM',
                    lhacode = [ 1, 1 ])

RCKM2x2 = Parameter(name = 'RCKM2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM2x2}',
                    lhablock = 'VCKM',
                    lhacode = [ 2, 2 ])

RCKM3x3 = Parameter(name = 'RCKM3x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM3x3}',
                    lhablock = 'VCKM',
                    lhacode = [ 3, 3 ])

RVV1x1 = Parameter(name = 'RVV1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.972557835,
                   texname = '\\text{RVV1x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 1 ])

RVV1x2 = Parameter(name = 'RVV1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.232661249,
                   texname = '\\text{RVV1x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 2 ])

RVV2x1 = Parameter(name = 'RVV2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.232661249,
                   texname = '\\text{RVV2x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 1 ])

RVV2x2 = Parameter(name = 'RVV2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.972557835,
                   texname = '\\text{RVV2x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 2 ])

Ryd3x3 = Parameter(name = 'Ryd3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.138840206,
                   texname = '\\text{Ryd3x3}',
                   lhablock = 'YD',
                   lhacode = [ 3, 3 ])

Rye3x3 = Parameter(name = 'Rye3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.10089081,
                   texname = '\\text{Rye3x3}',
                   lhablock = 'YE',
                   lhacode = [ 3, 3 ])

Ryu3x3 = Parameter(name = 'Ryu3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.89284455,
                   texname = '\\text{Ryu3x3}',
                   lhablock = 'YU',
                   lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 79.8290131,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 96.6880686,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 181.088157,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = -363.756027,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 381.729382,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 181.696474,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 379.93932,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 607.713704,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MH01 = Parameter(name = 'MH01',
                 nature = 'external',
                 type = 'real',
                 value = 110.899057,
                 texname = '\\text{MH01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

MH02 = Parameter(name = 'MH02',
                 nature = 'external',
                 type = 'real',
                 value = 399.960116,
                 texname = '\\text{MH02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 399.583917,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 407.879012,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 37 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 175.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.88991651,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Msn1 = Parameter(name = 'Msn1',
                 nature = 'external',
                 type = 'real',
                 value = 185.258326,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 185.258326,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 184.708464,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 202.91569,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 202.91569,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 134.490864,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 144.102799,
                 texname = '\\text{Msl4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

Msl5 = Parameter(name = 'Msl5',
                 nature = 'external',
                 type = 'real',
                 value = 144.102799,
                 texname = '\\text{Msl5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000013 ])

Msl6 = Parameter(name = 'Msl6',
                 nature = 'external',
                 type = 'real',
                 value = 206.867805,
                 texname = '\\text{Msl6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000015 ])

Msu1 = Parameter(name = 'Msu1',
                 nature = 'external',
                 type = 'real',
                 value = 561.119014,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 561.119014,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 399.668493,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 549.259265,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 549.259265,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 585.785818,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 568.441109,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 568.441109,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 513.065179,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 545.228462,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 545.228462,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 543.726676,
                 texname = '\\text{Msd6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

Mgld = Parameter(name = 'Mgld',
                 nature = 'external',
                 type = 'real',
                 value = 1.e-13,
                 texname = '\\text{Mgld}',
                 lhablock = 'MASS',
                 lhacode = [ 1000049 ])

Mgrv = Parameter(name = 'Mgrv',
                 nature = 'external',
                 type = 'real',
                 value = 1.e-13,
                 texname = '\\text{Mgrv}',
                 lhablock = 'MASS',
                 lhacode = [ 1000039 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.41143316,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.00282196,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wneu1 = Parameter(name = 'Wneu1',
                  nature = 'external',
                  type = 'real',
                  value = 0.02,
                  texname = '\\text{Wneu1}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000022 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 0.0207770048,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 1.91598495,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 2.58585079,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 0.0170414503,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 2.4868951,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 5.50675438,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WH01 = Parameter(name = 'WH01',
                 nature = 'external',
                 type = 'real',
                 value = 0.00198610799,
                 texname = '\\text{WH01}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

WH02 = Parameter(name = 'WH02',
                 nature = 'external',
                 type = 'real',
                 value = 0.574801389,
                 texname = '\\text{WH02}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 0.632178488,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.546962813,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 37 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.56194983,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsn1 = Parameter(name = 'Wsn1',
                 nature = 'external',
                 type = 'real',
                 value = 0.149881634,
                 texname = '\\text{Wsn1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsn2 = Parameter(name = 'Wsn2',
                 nature = 'external',
                 type = 'real',
                 value = 0.149881634,
                 texname = '\\text{Wsn2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsn3 = Parameter(name = 'Wsn3',
                 nature = 'external',
                 type = 'real',
                 value = 0.147518977,
                 texname = '\\text{Wsn3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

Wsl1 = Parameter(name = 'Wsl1',
                 nature = 'external',
                 type = 'real',
                 value = 0.213682161,
                 texname = '\\text{Wsl1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

Wsl2 = Parameter(name = 'Wsl2',
                 nature = 'external',
                 type = 'real',
                 value = 0.213682161,
                 texname = '\\text{Wsl2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000013 ])

Wsl3 = Parameter(name = 'Wsl3',
                 nature = 'external',
                 type = 'real',
                 value = 0.148327268,
                 texname = '\\text{Wsl3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000015 ])

Wsl4 = Parameter(name = 'Wsl4',
                 nature = 'external',
                 type = 'real',
                 value = 0.216121626,
                 texname = '\\text{Wsl4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

Wsl5 = Parameter(name = 'Wsl5',
                 nature = 'external',
                 type = 'real',
                 value = 0.216121626,
                 texname = '\\text{Wsl5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000013 ])

Wsl6 = Parameter(name = 'Wsl6',
                 nature = 'external',
                 type = 'real',
                 value = 0.269906096,
                 texname = '\\text{Wsl6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000015 ])

Wsu1 = Parameter(name = 'Wsu1',
                 nature = 'external',
                 type = 'real',
                 value = 5.47719539,
                 texname = '\\text{Wsu1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

Wsu2 = Parameter(name = 'Wsu2',
                 nature = 'external',
                 type = 'real',
                 value = 5.47719539,
                 texname = '\\text{Wsu2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

Wsu3 = Parameter(name = 'Wsu3',
                 nature = 'external',
                 type = 'real',
                 value = 2.02159578,
                 texname = '\\text{Wsu3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

Wsu4 = Parameter(name = 'Wsu4',
                 nature = 'external',
                 type = 'real',
                 value = 1.15297292,
                 texname = '\\text{Wsu4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

Wsu5 = Parameter(name = 'Wsu5',
                 nature = 'external',
                 type = 'real',
                 value = 1.15297292,
                 texname = '\\text{Wsu5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

Wsu6 = Parameter(name = 'Wsu6',
                 nature = 'external',
                 type = 'real',
                 value = 7.37313275,
                 texname = '\\text{Wsu6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

Wsd1 = Parameter(name = 'Wsd1',
                 nature = 'external',
                 type = 'real',
                 value = 5.31278772,
                 texname = '\\text{Wsd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

Wsd2 = Parameter(name = 'Wsd2',
                 nature = 'external',
                 type = 'real',
                 value = 5.31278772,
                 texname = '\\text{Wsd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

Wsd3 = Parameter(name = 'Wsd3',
                 nature = 'external',
                 type = 'real',
                 value = 3.73627601,
                 texname = '\\text{Wsd3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

Wsd4 = Parameter(name = 'Wsd4',
                 nature = 'external',
                 type = 'real',
                 value = 0.285812308,
                 texname = '\\text{Wsd4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

Wsd5 = Parameter(name = 'Wsd5',
                 nature = 'external',
                 type = 'real',
                 value = 0.285812308,
                 texname = '\\text{Wsd5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

Wsd6 = Parameter(name = 'Wsd6',
                 nature = 'external',
                 type = 'real',
                 value = 0.801566294,
                 texname = '\\text{Wsd6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM1x1',
                   texname = '\\text{CKM1x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM2x2',
                   texname = '\\text{CKM2x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM3x3',
                   texname = '\\text{CKM3x3}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

mD21x1 = Parameter(name = 'mD21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD21x1',
                   texname = '\\text{mD21x1}')

mD22x2 = Parameter(name = 'mD22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD22x2',
                   texname = '\\text{mD22x2}')

mD23x3 = Parameter(name = 'mD23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD23x3',
                   texname = '\\text{mD23x3}')

mE21x1 = Parameter(name = 'mE21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE21x1',
                   texname = '\\text{mE21x1}')

mE22x2 = Parameter(name = 'mE22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE22x2',
                   texname = '\\text{mE22x2}')

mE23x3 = Parameter(name = 'mE23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE23x3',
                   texname = '\\text{mE23x3}')

mL21x1 = Parameter(name = 'mL21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL21x1',
                   texname = '\\text{mL21x1}')

mL22x2 = Parameter(name = 'mL22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL22x2',
                   texname = '\\text{mL22x2}')

mL23x3 = Parameter(name = 'mL23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL23x3',
                   texname = '\\text{mL23x3}')

mQ21x1 = Parameter(name = 'mQ21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ21x1',
                   texname = '\\text{mQ21x1}')

mQ22x2 = Parameter(name = 'mQ22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ22x2',
                   texname = '\\text{mQ22x2}')

mQ23x3 = Parameter(name = 'mQ23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ23x3',
                   texname = '\\text{mQ23x3}')

mU21x1 = Parameter(name = 'mU21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU21x1',
                   texname = '\\text{mU21x1}')

mU22x2 = Parameter(name = 'mU22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU22x2',
                   texname = '\\text{mU22x2}')

mU23x3 = Parameter(name = 'mU23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU23x3',
                   texname = '\\text{mU23x3}')

MUH = Parameter(name = 'MUH',
                nature = 'internal',
                type = 'complex',
                value = 'RMUH',
                texname = '\\mu')

Mx1 = Parameter(name = 'Mx1',
                nature = 'internal',
                type = 'complex',
                value = 'RMx1',
                texname = 'M_1')

Mx2 = Parameter(name = 'Mx2',
                nature = 'internal',
                type = 'complex',
                value = 'RMx2',
                texname = 'M_2')

Mx3 = Parameter(name = 'Mx3',
                nature = 'internal',
                type = 'complex',
                value = 'RMx3',
                texname = 'M_3')

NN1x1 = Parameter(name = 'NN1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x1',
                  texname = '\\text{NN1x1}')

NN1x2 = Parameter(name = 'NN1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x2',
                  texname = '\\text{NN1x2}')

NN1x3 = Parameter(name = 'NN1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x3',
                  texname = '\\text{NN1x3}')

NN1x4 = Parameter(name = 'NN1x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x4',
                  texname = '\\text{NN1x4}')

NN2x1 = Parameter(name = 'NN2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x1',
                  texname = '\\text{NN2x1}')

NN2x2 = Parameter(name = 'NN2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x2',
                  texname = '\\text{NN2x2}')

NN2x3 = Parameter(name = 'NN2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x3',
                  texname = '\\text{NN2x3}')

NN2x4 = Parameter(name = 'NN2x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x4',
                  texname = '\\text{NN2x4}')

NN3x1 = Parameter(name = 'NN3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x1',
                  texname = '\\text{NN3x1}')

NN3x2 = Parameter(name = 'NN3x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x2',
                  texname = '\\text{NN3x2}')

NN3x3 = Parameter(name = 'NN3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x3',
                  texname = '\\text{NN3x3}')

NN3x4 = Parameter(name = 'NN3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x4',
                  texname = '\\text{NN3x4}')

NN4x1 = Parameter(name = 'NN4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x1',
                  texname = '\\text{NN4x1}')

NN4x2 = Parameter(name = 'NN4x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x2',
                  texname = '\\text{NN4x2}')

NN4x3 = Parameter(name = 'NN4x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x3',
                  texname = '\\text{NN4x3}')

NN4x4 = Parameter(name = 'NN4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x4',
                  texname = '\\text{NN4x4}')

Rd1x1 = Parameter(name = 'Rd1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd1x1',
                  texname = '\\text{Rd1x1}')

Rd2x2 = Parameter(name = 'Rd2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd2x2',
                  texname = '\\text{Rd2x2}')

Rd3x3 = Parameter(name = 'Rd3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd3x3',
                  texname = '\\text{Rd3x3}')

Rd3x6 = Parameter(name = 'Rd3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd3x6',
                  texname = '\\text{Rd3x6}')

Rd4x4 = Parameter(name = 'Rd4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd4x4',
                  texname = '\\text{Rd4x4}')

Rd5x5 = Parameter(name = 'Rd5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd5x5',
                  texname = '\\text{Rd5x5}')

Rd6x3 = Parameter(name = 'Rd6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd6x3',
                  texname = '\\text{Rd6x3}')

Rd6x6 = Parameter(name = 'Rd6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd6x6',
                  texname = '\\text{Rd6x6}')

Rl1x1 = Parameter(name = 'Rl1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl1x1',
                  texname = '\\text{Rl1x1}')

Rl2x2 = Parameter(name = 'Rl2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl2x2',
                  texname = '\\text{Rl2x2}')

Rl3x3 = Parameter(name = 'Rl3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl3x3',
                  texname = '\\text{Rl3x3}')

Rl3x6 = Parameter(name = 'Rl3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl3x6',
                  texname = '\\text{Rl3x6}')

Rl4x4 = Parameter(name = 'Rl4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl4x4',
                  texname = '\\text{Rl4x4}')

Rl5x5 = Parameter(name = 'Rl5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl5x5',
                  texname = '\\text{Rl5x5}')

Rl6x3 = Parameter(name = 'Rl6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x3',
                  texname = '\\text{Rl6x3}')

Rl6x6 = Parameter(name = 'Rl6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x6',
                  texname = '\\text{Rl6x6}')

Rn1x1 = Parameter(name = 'Rn1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn1x1',
                  texname = '\\text{Rn1x1}')

Rn2x2 = Parameter(name = 'Rn2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn2x2',
                  texname = '\\text{Rn2x2}')

Rn3x3 = Parameter(name = 'Rn3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn3x3',
                  texname = '\\text{Rn3x3}')

Ru1x1 = Parameter(name = 'Ru1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu1x1',
                  texname = '\\text{Ru1x1}')

Ru2x2 = Parameter(name = 'Ru2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu2x2',
                  texname = '\\text{Ru2x2}')

Ru3x3 = Parameter(name = 'Ru3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu3x3',
                  texname = '\\text{Ru3x3}')

Ru3x6 = Parameter(name = 'Ru3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu3x6',
                  texname = '\\text{Ru3x6}')

Ru4x4 = Parameter(name = 'Ru4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu4x4',
                  texname = '\\text{Ru4x4}')

Ru5x5 = Parameter(name = 'Ru5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu5x5',
                  texname = '\\text{Ru5x5}')

Ru6x3 = Parameter(name = 'Ru6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu6x3',
                  texname = '\\text{Ru6x3}')

Ru6x6 = Parameter(name = 'Ru6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu6x6',
                  texname = '\\text{Ru6x6}')

UU1x1 = Parameter(name = 'UU1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x1',
                  texname = '\\text{UU1x1}')

UU1x2 = Parameter(name = 'UU1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x2',
                  texname = '\\text{UU1x2}')

UU2x1 = Parameter(name = 'UU2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x1',
                  texname = '\\text{UU2x1}')

UU2x2 = Parameter(name = 'UU2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x2',
                  texname = '\\text{UU2x2}')

VV1x1 = Parameter(name = 'VV1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x1',
                  texname = '\\text{VV1x1}')

VV1x2 = Parameter(name = 'VV1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x2',
                  texname = '\\text{VV1x2}')

VV2x1 = Parameter(name = 'VV2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x1',
                  texname = '\\text{VV2x1}')

VV2x2 = Parameter(name = 'VV2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x2',
                  texname = '\\text{VV2x2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

td3x3 = Parameter(name = 'td3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtd3x3',
                  texname = '\\text{td3x3}')

te3x3 = Parameter(name = 'te3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rte3x3',
                  texname = '\\text{te3x3}')

tu3x3 = Parameter(name = 'tu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtu3x3',
                  texname = '\\text{tu3x3}')

yd3x3 = Parameter(name = 'yd3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryd3x3',
                  texname = '\\text{yd3x3}')

ye3x3 = Parameter(name = 'ye3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rye3x3',
                  texname = '\\text{ye3x3}')

yu3x3 = Parameter(name = 'yu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryu3x3',
                  texname = '\\text{yu3x3}')

bb = Parameter(name = 'bb',
               nature = 'internal',
               type = 'complex',
               value = '((-mHd2 + mHu2)*cmath.tan(2*alp))/2. - MZ**2*(cmath.sin(2*beta)/2. + cmath.cos(2*beta)*cmath.tan(2*alp))',
               texname = 'b')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

I1b33 = Parameter(name = 'I1b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                  texname = '\\text{I1b33}')

I10b33 = Parameter(name = 'I10b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I10b33}')

I10b36 = Parameter(name = 'I10b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(yd3x3)',
                   texname = '\\text{I10b36}')

I100b33 = Parameter(name = 'I100b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*complexconjugate(Rd3x6)',
                    texname = '\\text{I100b33}')

I100b36 = Parameter(name = 'I100b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*complexconjugate(Rd3x6)',
                    texname = '\\text{I100b36}')

I100b44 = Parameter(name = 'I100b44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*complexconjugate(Rd4x4)',
                    texname = '\\text{I100b44}')

I100b55 = Parameter(name = 'I100b55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x5*complexconjugate(Rd5x5)',
                    texname = '\\text{I100b55}')

I100b63 = Parameter(name = 'I100b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*complexconjugate(Rd6x6)',
                    texname = '\\text{I100b63}')

I100b66 = Parameter(name = 'I100b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*complexconjugate(Rd6x6)',
                    texname = '\\text{I100b66}')

I101b33 = Parameter(name = 'I101b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*complexconjugate(Rl3x6)',
                    texname = '\\text{I101b33}')

I101b36 = Parameter(name = 'I101b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl3x6)',
                    texname = '\\text{I101b36}')

I101b44 = Parameter(name = 'I101b44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x4*complexconjugate(Rl4x4)',
                    texname = '\\text{I101b44}')

I101b55 = Parameter(name = 'I101b55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x5*complexconjugate(Rl5x5)',
                    texname = '\\text{I101b55}')

I101b63 = Parameter(name = 'I101b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I101b63}')

I101b66 = Parameter(name = 'I101b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I101b66}')

I102b33 = Parameter(name = 'I102b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I102b33}')

I102b36 = Parameter(name = 'I102b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I102b36}')

I102b44 = Parameter(name = 'I102b44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*complexconjugate(Ru4x4)',
                    texname = '\\text{I102b44}')

I102b55 = Parameter(name = 'I102b55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x5*complexconjugate(Ru5x5)',
                    texname = '\\text{I102b55}')

I102b63 = Parameter(name = 'I102b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I102b63}')

I102b66 = Parameter(name = 'I102b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I102b66}')

I103b11 = Parameter(name = 'I103b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn1x1)',
                    texname = '\\text{I103b11}')

I103b22 = Parameter(name = 'I103b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn2x2)',
                    texname = '\\text{I103b22}')

I103b33 = Parameter(name = 'I103b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn3x3)',
                    texname = '\\text{I103b33}')

I104b11 = Parameter(name = 'I104b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I104b11}')

I104b22 = Parameter(name = 'I104b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I104b22}')

I104b33 = Parameter(name = 'I104b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I104b33}')

I104b36 = Parameter(name = 'I104b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I104b36}')

I105b33 = Parameter(name = 'I105b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3',
                    texname = '\\text{I105b33}')

I105b36 = Parameter(name = 'I105b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3',
                    texname = '\\text{I105b36}')

I106b33 = Parameter(name = 'I106b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(yd3x3)',
                    texname = '\\text{I106b33}')

I106b36 = Parameter(name = 'I106b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(yd3x3)',
                    texname = '\\text{I106b36}')

I107b33 = Parameter(name = 'I107b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)',
                    texname = '\\text{I107b33}')

I107b36 = Parameter(name = 'I107b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)',
                    texname = '\\text{I107b36}')

I108b33 = Parameter(name = 'I108b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I108b33}')

I108b36 = Parameter(name = 'I108b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I108b36}')

I109b33 = Parameter(name = 'I109b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3',
                    texname = '\\text{I109b33}')

I109b36 = Parameter(name = 'I109b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3',
                    texname = '\\text{I109b36}')

I11b33 = Parameter(name = 'I11b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3',
                   texname = '\\text{I11b33}')

I11b36 = Parameter(name = 'I11b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3',
                   texname = '\\text{I11b36}')

I110b33 = Parameter(name = 'I110b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(ye3x3)',
                    texname = '\\text{I110b33}')

I110b36 = Parameter(name = 'I110b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(ye3x3)',
                    texname = '\\text{I110b36}')

I111b33 = Parameter(name = 'I111b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3',
                    texname = '\\text{I111b33}')

I111b36 = Parameter(name = 'I111b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3',
                    texname = '\\text{I111b36}')

I112b33 = Parameter(name = 'I112b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3',
                    texname = '\\text{I112b33}')

I112b36 = Parameter(name = 'I112b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3',
                    texname = '\\text{I112b36}')

I113b33 = Parameter(name = 'I113b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(yd3x3)',
                    texname = '\\text{I113b33}')

I113b36 = Parameter(name = 'I113b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(yd3x3)',
                    texname = '\\text{I113b36}')

I114b33 = Parameter(name = 'I114b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3',
                    texname = '\\text{I114b33}')

I114b36 = Parameter(name = 'I114b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3',
                    texname = '\\text{I114b36}')

I115b33 = Parameter(name = 'I115b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(yu3x3)',
                    texname = '\\text{I115b33}')

I115b36 = Parameter(name = 'I115b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(yu3x3)',
                    texname = '\\text{I115b36}')

I116b11 = Parameter(name = 'I116b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x1*complexconjugate(Rl1x1)',
                    texname = '\\text{I116b11}')

I116b22 = Parameter(name = 'I116b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(Rl2x2)',
                    texname = '\\text{I116b22}')

I116b33 = Parameter(name = 'I116b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I116b33}')

I116b36 = Parameter(name = 'I116b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I116b36}')

I117b33 = Parameter(name = 'I117b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I117b33}')

I117b36 = Parameter(name = 'I117b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I117b36}')

I118b11 = Parameter(name = 'I118b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                    texname = '\\text{I118b11}')

I118b22 = Parameter(name = 'I118b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                    texname = '\\text{I118b22}')

I118b33 = Parameter(name = 'I118b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I118b33}')

I118b36 = Parameter(name = 'I118b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I118b36}')

I118b63 = Parameter(name = 'I118b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I118b63}')

I118b66 = Parameter(name = 'I118b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I118b66}')

I119b33 = Parameter(name = 'I119b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I119b33}')

I119b36 = Parameter(name = 'I119b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I119b36}')

I119b63 = Parameter(name = 'I119b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I119b63}')

I119b66 = Parameter(name = 'I119b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I119b66}')

I12b11 = Parameter(name = 'I12b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I12b11}')

I12b22 = Parameter(name = 'I12b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I12b22}')

I12b33 = Parameter(name = 'I12b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I12b33}')

I12b36 = Parameter(name = 'I12b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I12b36}')

I120b33 = Parameter(name = 'I120b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I120b33}')

I120b36 = Parameter(name = 'I120b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I120b36}')

I120b63 = Parameter(name = 'I120b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I120b63}')

I120b66 = Parameter(name = 'I120b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I120b66}')

I121b33 = Parameter(name = 'I121b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I121b33}')

I121b36 = Parameter(name = 'I121b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I121b36}')

I121b63 = Parameter(name = 'I121b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I121b63}')

I121b66 = Parameter(name = 'I121b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I121b66}')

I122b33 = Parameter(name = 'I122b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122b33}')

I122b36 = Parameter(name = 'I122b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122b36}')

I122b63 = Parameter(name = 'I122b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122b63}')

I122b66 = Parameter(name = 'I122b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122b66}')

I123b33 = Parameter(name = 'I123b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I123b33}')

I123b36 = Parameter(name = 'I123b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I123b36}')

I123b63 = Parameter(name = 'I123b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I123b63}')

I123b66 = Parameter(name = 'I123b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I123b66}')

I124b33 = Parameter(name = 'I124b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I124b33}')

I124b36 = Parameter(name = 'I124b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I124b36}')

I124b63 = Parameter(name = 'I124b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I124b63}')

I124b66 = Parameter(name = 'I124b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I124b66}')

I125b33 = Parameter(name = 'I125b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I125b33}')

I125b36 = Parameter(name = 'I125b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I125b36}')

I125b63 = Parameter(name = 'I125b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I125b63}')

I125b66 = Parameter(name = 'I125b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I125b66}')

I126b33 = Parameter(name = 'I126b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126b33}')

I126b36 = Parameter(name = 'I126b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126b36}')

I126b63 = Parameter(name = 'I126b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126b63}')

I126b66 = Parameter(name = 'I126b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126b66}')

I127b33 = Parameter(name = 'I127b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I127b33}')

I127b36 = Parameter(name = 'I127b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I127b36}')

I128b33 = Parameter(name = 'I128b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I128b33}')

I128b36 = Parameter(name = 'I128b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I128b36}')

I129b33 = Parameter(name = 'I129b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I129b33}')

I129b36 = Parameter(name = 'I129b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I129b36}')

I13b33 = Parameter(name = 'I13b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I13b33}')

I13b36 = Parameter(name = 'I13b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I13b36}')

I130b33 = Parameter(name = 'I130b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I130b33}')

I130b36 = Parameter(name = 'I130b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I130b36}')

I131b33 = Parameter(name = 'I131b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I131b33}')

I131b36 = Parameter(name = 'I131b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I131b36}')

I132b33 = Parameter(name = 'I132b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I132b33}')

I132b36 = Parameter(name = 'I132b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I132b36}')

I133b33 = Parameter(name = 'I133b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I133b33}')

I133b36 = Parameter(name = 'I133b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I133b36}')

I134b33 = Parameter(name = 'I134b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I134b33}')

I134b36 = Parameter(name = 'I134b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I134b36}')

I135b33 = Parameter(name = 'I135b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I135b33}')

I135b36 = Parameter(name = 'I135b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I135b36}')

I136b33 = Parameter(name = 'I136b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136b33}')

I136b36 = Parameter(name = 'I136b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136b36}')

I137b33 = Parameter(name = 'I137b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I137b33}')

I137b36 = Parameter(name = 'I137b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I137b36}')

I138b11 = Parameter(name = 'I138b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x1*complexconjugate(Rn1x1)',
                    texname = '\\text{I138b11}')

I138b22 = Parameter(name = 'I138b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I138b22}')

I138b33 = Parameter(name = 'I138b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I138b33}')

I138b36 = Parameter(name = 'I138b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I138b36}')

I139b33 = Parameter(name = 'I139b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I139b33}')

I139b36 = Parameter(name = 'I139b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I139b36}')

I14b33 = Parameter(name = 'I14b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I14b33}')

I14b36 = Parameter(name = 'I14b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I14b36}')

I140b11 = Parameter(name = 'I140b11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I140b11}')

I140b22 = Parameter(name = 'I140b22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I140b22}')

I140b33 = Parameter(name = 'I140b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I140b33}')

I140b36 = Parameter(name = 'I140b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I140b36}')

I140b63 = Parameter(name = 'I140b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I140b63}')

I140b66 = Parameter(name = 'I140b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I140b66}')

I141b33 = Parameter(name = 'I141b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I141b33}')

I141b36 = Parameter(name = 'I141b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I141b36}')

I141b63 = Parameter(name = 'I141b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I141b63}')

I141b66 = Parameter(name = 'I141b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I141b66}')

I142b33 = Parameter(name = 'I142b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I142b33}')

I142b36 = Parameter(name = 'I142b36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I142b36}')

I142b63 = Parameter(name = 'I142b63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I142b63}')

I142b66 = Parameter(name = 'I142b66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I142b66}')

I143b33 = Parameter(name = 'I143b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I143b33}')

I144b33 = Parameter(name = 'I144b33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(ye3x3)',
                    texname = '\\text{I144b33}')

I15b11 = Parameter(name = 'I15b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I15b11}')

I15b22 = Parameter(name = 'I15b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I15b22}')

I15b33 = Parameter(name = 'I15b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I15b33}')

I15b36 = Parameter(name = 'I15b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I15b36}')

I15b63 = Parameter(name = 'I15b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I15b63}')

I15b66 = Parameter(name = 'I15b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I15b66}')

I16b33 = Parameter(name = 'I16b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I16b33}')

I16b36 = Parameter(name = 'I16b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I16b36}')

I16b44 = Parameter(name = 'I16b44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I16b44}')

I16b55 = Parameter(name = 'I16b55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I16b55}')

I16b63 = Parameter(name = 'I16b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I16b63}')

I16b66 = Parameter(name = 'I16b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I16b66}')

I17b33 = Parameter(name = 'I17b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I17b33}')

I17b36 = Parameter(name = 'I17b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I17b36}')

I17b63 = Parameter(name = 'I17b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I17b63}')

I17b66 = Parameter(name = 'I17b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I17b66}')

I18b33 = Parameter(name = 'I18b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I18b33}')

I18b36 = Parameter(name = 'I18b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I18b36}')

I18b63 = Parameter(name = 'I18b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I18b63}')

I18b66 = Parameter(name = 'I18b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I18b66}')

I19b33 = Parameter(name = 'I19b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I19b33}')

I19b36 = Parameter(name = 'I19b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I19b36}')

I19b63 = Parameter(name = 'I19b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I19b63}')

I19b66 = Parameter(name = 'I19b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I19b66}')

I2b33 = Parameter(name = 'I2b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I2b33}')

I20b33 = Parameter(name = 'I20b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I20b33}')

I20b36 = Parameter(name = 'I20b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I20b36}')

I20b63 = Parameter(name = 'I20b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I20b63}')

I20b66 = Parameter(name = 'I20b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I20b66}')

I21b33 = Parameter(name = 'I21b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I21b33}')

I21b36 = Parameter(name = 'I21b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I21b36}')

I21b63 = Parameter(name = 'I21b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I21b63}')

I21b66 = Parameter(name = 'I21b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I21b66}')

I22b33 = Parameter(name = 'I22b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I22b33}')

I22b36 = Parameter(name = 'I22b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I22b36}')

I22b63 = Parameter(name = 'I22b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I22b63}')

I22b66 = Parameter(name = 'I22b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I22b66}')

I23b33 = Parameter(name = 'I23b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I23b33}')

I23b36 = Parameter(name = 'I23b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I23b36}')

I24b33 = Parameter(name = 'I24b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I24b33}')

I24b36 = Parameter(name = 'I24b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I24b36}')

I25b11 = Parameter(name = 'I25b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I25b11}')

I25b22 = Parameter(name = 'I25b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I25b22}')

I25b33 = Parameter(name = 'I25b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I25b33}')

I25b36 = Parameter(name = 'I25b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I25b36}')

I25b63 = Parameter(name = 'I25b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I25b63}')

I25b66 = Parameter(name = 'I25b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I25b66}')

I26b33 = Parameter(name = 'I26b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I26b33}')

I26b36 = Parameter(name = 'I26b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I26b36}')

I26b44 = Parameter(name = 'I26b44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I26b44}')

I26b55 = Parameter(name = 'I26b55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I26b55}')

I26b63 = Parameter(name = 'I26b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I26b63}')

I26b66 = Parameter(name = 'I26b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I26b66}')

I27b33 = Parameter(name = 'I27b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(ye3x3)',
                   texname = '\\text{I27b33}')

I27b36 = Parameter(name = 'I27b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(ye3x3)',
                   texname = '\\text{I27b36}')

I28b33 = Parameter(name = 'I28b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3',
                   texname = '\\text{I28b33}')

I28b36 = Parameter(name = 'I28b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I28b36}')

I29b11 = Parameter(name = 'I29b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1',
                   texname = '\\text{I29b11}')

I29b22 = Parameter(name = 'I29b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2',
                   texname = '\\text{I29b22}')

I29b33 = Parameter(name = 'I29b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3',
                   texname = '\\text{I29b33}')

I29b36 = Parameter(name = 'I29b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3',
                   texname = '\\text{I29b36}')

I3b33 = Parameter(name = 'I3b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*complexconjugate(yd3x3)',
                  texname = '\\text{I3b33}')

I30b33 = Parameter(name = 'I30b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3',
                   texname = '\\text{I30b33}')

I30b36 = Parameter(name = 'I30b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I30b36}')

I31b11 = Parameter(name = 'I31b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I31b11}')

I31b22 = Parameter(name = 'I31b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I31b22}')

I31b33 = Parameter(name = 'I31b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I31b33}')

I31b36 = Parameter(name = 'I31b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I31b36}')

I31b63 = Parameter(name = 'I31b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I31b63}')

I31b66 = Parameter(name = 'I31b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I31b66}')

I32b33 = Parameter(name = 'I32b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I32b33}')

I32b36 = Parameter(name = 'I32b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I32b36}')

I32b44 = Parameter(name = 'I32b44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I32b44}')

I32b55 = Parameter(name = 'I32b55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I32b55}')

I32b63 = Parameter(name = 'I32b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I32b63}')

I32b66 = Parameter(name = 'I32b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I32b66}')

I33b33 = Parameter(name = 'I33b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                   texname = '\\text{I33b33}')

I33b36 = Parameter(name = 'I33b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                   texname = '\\text{I33b36}')

I33b63 = Parameter(name = 'I33b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I33b63}')

I33b66 = Parameter(name = 'I33b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I33b66}')

I34b33 = Parameter(name = 'I34b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I34b33}')

I34b36 = Parameter(name = 'I34b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I34b36}')

I34b63 = Parameter(name = 'I34b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I34b63}')

I34b66 = Parameter(name = 'I34b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I34b66}')

I35b33 = Parameter(name = 'I35b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I35b33}')

I35b36 = Parameter(name = 'I35b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I35b36}')

I35b63 = Parameter(name = 'I35b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I35b63}')

I35b66 = Parameter(name = 'I35b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I35b66}')

I36b33 = Parameter(name = 'I36b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I36b33}')

I36b36 = Parameter(name = 'I36b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I36b36}')

I36b63 = Parameter(name = 'I36b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I36b63}')

I36b66 = Parameter(name = 'I36b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I36b66}')

I37b33 = Parameter(name = 'I37b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I37b33}')

I37b36 = Parameter(name = 'I37b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I37b36}')

I37b63 = Parameter(name = 'I37b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I37b63}')

I37b66 = Parameter(name = 'I37b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I37b66}')

I38b33 = Parameter(name = 'I38b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I38b33}')

I38b36 = Parameter(name = 'I38b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I38b36}')

I38b63 = Parameter(name = 'I38b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I38b63}')

I38b66 = Parameter(name = 'I38b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I38b66}')

I39b11 = Parameter(name = 'I39b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rn1x1)',
                   texname = '\\text{I39b11}')

I39b22 = Parameter(name = 'I39b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I39b22}')

I39b33 = Parameter(name = 'I39b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I39b33}')

I39b36 = Parameter(name = 'I39b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I39b36}')

I4b33 = Parameter(name = 'I4b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yu3x3',
                  texname = '\\text{I4b33}')

I40b33 = Parameter(name = 'I40b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I40b33}')

I40b36 = Parameter(name = 'I40b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I40b36}')

I41b33 = Parameter(name = 'I41b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rn3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I41b33}')

I41b36 = Parameter(name = 'I41b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rn3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I41b36}')

I42b33 = Parameter(name = 'I42b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I42b33}')

I42b36 = Parameter(name = 'I42b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I42b36}')

I43b11 = Parameter(name = 'I43b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x1',
                   texname = '\\text{I43b11}')

I43b22 = Parameter(name = 'I43b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2',
                   texname = '\\text{I43b22}')

I43b33 = Parameter(name = 'I43b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3',
                   texname = '\\text{I43b33}')

I44b33 = Parameter(name = 'I44b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(ye3x3)',
                   texname = '\\text{I44b33}')

I45b11 = Parameter(name = 'I45b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I45b11}')

I45b22 = Parameter(name = 'I45b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I45b22}')

I45b33 = Parameter(name = 'I45b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I45b33}')

I45b36 = Parameter(name = 'I45b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I45b36}')

I46b33 = Parameter(name = 'I46b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                   texname = '\\text{I46b33}')

I46b36 = Parameter(name = 'I46b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I46b36}')

I47b33 = Parameter(name = 'I47b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I47b33}')

I47b36 = Parameter(name = 'I47b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I47b36}')

I48b33 = Parameter(name = 'I48b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I48b33}')

I48b36 = Parameter(name = 'I48b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I48b36}')

I49b33 = Parameter(name = 'I49b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I49b33}')

I49b36 = Parameter(name = 'I49b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I49b36}')

I5b33 = Parameter(name = 'I5b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(ye3x3)',
                  texname = '\\text{I5b33}')

I50b33 = Parameter(name = 'I50b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I50b33}')

I50b36 = Parameter(name = 'I50b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I50b36}')

I51b11 = Parameter(name = 'I51b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x1*complexconjugate(Ru1x1)',
                   texname = '\\text{I51b11}')

I51b22 = Parameter(name = 'I51b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x2*complexconjugate(Ru2x2)',
                   texname = '\\text{I51b22}')

I51b33 = Parameter(name = 'I51b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I51b33}')

I51b36 = Parameter(name = 'I51b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I51b36}')

I51b63 = Parameter(name = 'I51b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I51b63}')

I51b66 = Parameter(name = 'I51b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I51b66}')

I52b33 = Parameter(name = 'I52b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I52b33}')

I52b36 = Parameter(name = 'I52b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I52b36}')

I52b44 = Parameter(name = 'I52b44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I52b44}')

I52b55 = Parameter(name = 'I52b55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x5*complexconjugate(Ru5x5)',
                   texname = '\\text{I52b55}')

I52b63 = Parameter(name = 'I52b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I52b63}')

I52b66 = Parameter(name = 'I52b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I52b66}')

I53b11 = Parameter(name = 'I53b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                   texname = '\\text{I53b11}')

I53b22 = Parameter(name = 'I53b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                   texname = '\\text{I53b22}')

I53b33 = Parameter(name = 'I53b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I53b33}')

I53b36 = Parameter(name = 'I53b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I53b36}')

I53b63 = Parameter(name = 'I53b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I53b63}')

I53b66 = Parameter(name = 'I53b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I53b66}')

I54b33 = Parameter(name = 'I54b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I54b33}')

I54b36 = Parameter(name = 'I54b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I54b36}')

I54b63 = Parameter(name = 'I54b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I54b63}')

I54b66 = Parameter(name = 'I54b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I54b66}')

I55b33 = Parameter(name = 'I55b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I55b33}')

I55b36 = Parameter(name = 'I55b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I55b36}')

I55b63 = Parameter(name = 'I55b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I55b63}')

I55b66 = Parameter(name = 'I55b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I55b66}')

I56b33 = Parameter(name = 'I56b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I56b33}')

I56b36 = Parameter(name = 'I56b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I56b36}')

I56b63 = Parameter(name = 'I56b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I56b63}')

I56b66 = Parameter(name = 'I56b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I56b66}')

I57b33 = Parameter(name = 'I57b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I57b33}')

I57b36 = Parameter(name = 'I57b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I57b36}')

I57b63 = Parameter(name = 'I57b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I57b63}')

I57b66 = Parameter(name = 'I57b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I57b66}')

I58b33 = Parameter(name = 'I58b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I58b33}')

I58b36 = Parameter(name = 'I58b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I58b36}')

I58b63 = Parameter(name = 'I58b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I58b63}')

I58b66 = Parameter(name = 'I58b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I58b66}')

I59b33 = Parameter(name = 'I59b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I59b33}')

I59b36 = Parameter(name = 'I59b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I59b36}')

I59b63 = Parameter(name = 'I59b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I59b63}')

I59b66 = Parameter(name = 'I59b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I59b66}')

I6b33 = Parameter(name = 'I6b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                  texname = '\\text{I6b33}')

I6b36 = Parameter(name = 'I6b36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                  texname = '\\text{I6b36}')

I60b33 = Parameter(name = 'I60b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I60b33}')

I60b36 = Parameter(name = 'I60b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I60b36}')

I60b63 = Parameter(name = 'I60b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I60b63}')

I60b66 = Parameter(name = 'I60b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I60b66}')

I61b33 = Parameter(name = 'I61b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(yu3x3)',
                   texname = '\\text{I61b33}')

I61b36 = Parameter(name = 'I61b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(yu3x3)',
                   texname = '\\text{I61b36}')

I62b33 = Parameter(name = 'I62b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3',
                   texname = '\\text{I62b33}')

I62b36 = Parameter(name = 'I62b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3',
                   texname = '\\text{I62b36}')

I63b11 = Parameter(name = 'I63b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Ru1x1',
                   texname = '\\text{I63b11}')

I63b22 = Parameter(name = 'I63b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Ru2x2',
                   texname = '\\text{I63b22}')

I63b33 = Parameter(name = 'I63b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3',
                   texname = '\\text{I63b33}')

I63b36 = Parameter(name = 'I63b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3',
                   texname = '\\text{I63b36}')

I64b33 = Parameter(name = 'I64b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I64b33}')

I64b36 = Parameter(name = 'I64b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(yd3x3)',
                   texname = '\\text{I64b36}')

I65b33 = Parameter(name = 'I65b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3',
                   texname = '\\text{I65b33}')

I65b36 = Parameter(name = 'I65b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3',
                   texname = '\\text{I65b36}')

I66b11 = Parameter(name = 'I66b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I66b11}')

I66b22 = Parameter(name = 'I66b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I66b22}')

I66b33 = Parameter(name = 'I66b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I66b33}')

I66b36 = Parameter(name = 'I66b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I66b36}')

I66b63 = Parameter(name = 'I66b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I66b63}')

I66b66 = Parameter(name = 'I66b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I66b66}')

I67b33 = Parameter(name = 'I67b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I67b33}')

I67b36 = Parameter(name = 'I67b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I67b36}')

I67b63 = Parameter(name = 'I67b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I67b63}')

I67b66 = Parameter(name = 'I67b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I67b66}')

I68b33 = Parameter(name = 'I68b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I68b33}')

I68b36 = Parameter(name = 'I68b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I68b36}')

I68b63 = Parameter(name = 'I68b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I68b63}')

I68b66 = Parameter(name = 'I68b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I68b66}')

I69b33 = Parameter(name = 'I69b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*tu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I69b33}')

I69b36 = Parameter(name = 'I69b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*tu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I69b36}')

I69b63 = Parameter(name = 'I69b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*tu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I69b63}')

I69b66 = Parameter(name = 'I69b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*tu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I69b66}')

I7b33 = Parameter(name = 'I7b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3*complexconjugate(Rd3x3)',
                  texname = '\\text{I7b33}')

I7b36 = Parameter(name = 'I7b36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3*complexconjugate(Rd6x3)',
                  texname = '\\text{I7b36}')

I70b33 = Parameter(name = 'I70b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I70b33}')

I70b36 = Parameter(name = 'I70b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I70b36}')

I70b63 = Parameter(name = 'I70b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I70b63}')

I70b66 = Parameter(name = 'I70b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I70b66}')

I71b33 = Parameter(name = 'I71b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I71b33}')

I71b36 = Parameter(name = 'I71b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I71b36}')

I71b63 = Parameter(name = 'I71b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I71b63}')

I71b66 = Parameter(name = 'I71b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I71b66}')

I72b33 = Parameter(name = 'I72b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*yu3x3*complexconjugate(Rd3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I72b33}')

I72b36 = Parameter(name = 'I72b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*yu3x3*complexconjugate(Rd3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I72b36}')

I72b63 = Parameter(name = 'I72b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*yu3x3*complexconjugate(Rd6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I72b63}')

I72b66 = Parameter(name = 'I72b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*yu3x3*complexconjugate(Rd6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I72b66}')

I73b33 = Parameter(name = 'I73b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I73b33}')

I73b36 = Parameter(name = 'I73b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I73b36}')

I73b63 = Parameter(name = 'I73b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I73b63}')

I73b66 = Parameter(name = 'I73b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I73b66}')

I74b11 = Parameter(name = 'I74b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x1*complexconjugate(Ru1x1)',
                   texname = '\\text{I74b11}')

I74b22 = Parameter(name = 'I74b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x2*complexconjugate(Ru2x2)',
                   texname = '\\text{I74b22}')

I74b33 = Parameter(name = 'I74b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I74b33}')

I74b36 = Parameter(name = 'I74b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I74b36}')

I74b63 = Parameter(name = 'I74b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I74b63}')

I74b66 = Parameter(name = 'I74b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I74b66}')

I75b33 = Parameter(name = 'I75b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I75b33}')

I75b36 = Parameter(name = 'I75b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I75b36}')

I75b44 = Parameter(name = 'I75b44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I75b44}')

I75b55 = Parameter(name = 'I75b55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x5*complexconjugate(Ru5x5)',
                   texname = '\\text{I75b55}')

I75b63 = Parameter(name = 'I75b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I75b63}')

I75b66 = Parameter(name = 'I75b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I75b66}')

I76b33 = Parameter(name = 'I76b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I76b33}')

I76b36 = Parameter(name = 'I76b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I76b36}')

I76b63 = Parameter(name = 'I76b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I76b63}')

I76b66 = Parameter(name = 'I76b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I76b66}')

I77b33 = Parameter(name = 'I77b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I77b33}')

I77b36 = Parameter(name = 'I77b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I77b36}')

I77b63 = Parameter(name = 'I77b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I77b63}')

I77b66 = Parameter(name = 'I77b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I77b66}')

I78b33 = Parameter(name = 'I78b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*tu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I78b33}')

I78b36 = Parameter(name = 'I78b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*tu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I78b36}')

I78b63 = Parameter(name = 'I78b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*tu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I78b63}')

I78b66 = Parameter(name = 'I78b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*tu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I78b66}')

I79b33 = Parameter(name = 'I79b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I79b33}')

I79b36 = Parameter(name = 'I79b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I79b36}')

I79b63 = Parameter(name = 'I79b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I79b63}')

I79b66 = Parameter(name = 'I79b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I79b66}')

I8b11 = Parameter(name = 'I8b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x1*complexconjugate(Rd1x1)',
                  texname = '\\text{I8b11}')

I8b22 = Parameter(name = 'I8b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x2*complexconjugate(Rd2x2)',
                  texname = '\\text{I8b22}')

I8b33 = Parameter(name = 'I8b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x3*complexconjugate(Rd3x3)',
                  texname = '\\text{I8b33}')

I8b36 = Parameter(name = 'I8b36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x3*complexconjugate(Rd3x3)',
                  texname = '\\text{I8b36}')

I8b63 = Parameter(name = 'I8b63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x3*complexconjugate(Rd6x3)',
                  texname = '\\text{I8b63}')

I8b66 = Parameter(name = 'I8b66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x3*complexconjugate(Rd6x3)',
                  texname = '\\text{I8b66}')

I80b33 = Parameter(name = 'I80b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*yu3x3*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I80b33}')

I80b36 = Parameter(name = 'I80b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*yu3x3*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I80b36}')

I80b63 = Parameter(name = 'I80b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*yu3x3*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I80b63}')

I80b66 = Parameter(name = 'I80b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*yu3x3*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I80b66}')

I81b33 = Parameter(name = 'I81b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81b33}')

I81b36 = Parameter(name = 'I81b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81b36}')

I81b63 = Parameter(name = 'I81b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81b63}')

I81b66 = Parameter(name = 'I81b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81b66}')

I82b11 = Parameter(name = 'I82b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I82b11}')

I82b22 = Parameter(name = 'I82b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I82b22}')

I82b33 = Parameter(name = 'I82b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I82b33}')

I82b36 = Parameter(name = 'I82b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I82b36}')

I83b33 = Parameter(name = 'I83b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I83b33}')

I83b36 = Parameter(name = 'I83b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I83b36}')

I84b33 = Parameter(name = 'I84b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I84b33}')

I84b36 = Parameter(name = 'I84b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I84b36}')

I85b11 = Parameter(name = 'I85b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl1x1)',
                   texname = '\\text{I85b11}')

I85b22 = Parameter(name = 'I85b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl2x2)',
                   texname = '\\text{I85b22}')

I85b33 = Parameter(name = 'I85b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x3)',
                   texname = '\\text{I85b33}')

I85b36 = Parameter(name = 'I85b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x3)',
                   texname = '\\text{I85b36}')

I86b33 = Parameter(name = 'I86b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86b33}')

I86b36 = Parameter(name = 'I86b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86b36}')

I87b11 = Parameter(name = 'I87b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn1x1)',
                   texname = '\\text{I87b11}')

I87b22 = Parameter(name = 'I87b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn2x2)',
                   texname = '\\text{I87b22}')

I87b33 = Parameter(name = 'I87b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn3x3)',
                   texname = '\\text{I87b33}')

I88b33 = Parameter(name = 'I88b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I88b33}')

I89b11 = Parameter(name = 'I89b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                   texname = '\\text{I89b11}')

I89b22 = Parameter(name = 'I89b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                   texname = '\\text{I89b22}')

I89b33 = Parameter(name = 'I89b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I89b33}')

I89b36 = Parameter(name = 'I89b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I89b36}')

I9b33 = Parameter(name = 'I9b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x6*complexconjugate(Rd3x6)',
                  texname = '\\text{I9b33}')

I9b36 = Parameter(name = 'I9b36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x6*complexconjugate(Rd3x6)',
                  texname = '\\text{I9b36}')

I9b44 = Parameter(name = 'I9b44',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd4x4*complexconjugate(Rd4x4)',
                  texname = '\\text{I9b44}')

I9b55 = Parameter(name = 'I9b55',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd5x5*complexconjugate(Rd5x5)',
                  texname = '\\text{I9b55}')

I9b63 = Parameter(name = 'I9b63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x6*complexconjugate(Rd6x6)',
                  texname = '\\text{I9b63}')

I9b66 = Parameter(name = 'I9b66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x6*complexconjugate(Rd6x6)',
                  texname = '\\text{I9b66}')

I90b33 = Parameter(name = 'I90b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I90b33}')

I90b36 = Parameter(name = 'I90b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I90b36}')

I91b33 = Parameter(name = 'I91b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I91b33}')

I91b36 = Parameter(name = 'I91b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I91b36}')

I92b11 = Parameter(name = 'I92b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I92b11}')

I92b22 = Parameter(name = 'I92b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I92b22}')

I92b33 = Parameter(name = 'I92b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I92b33}')

I92b36 = Parameter(name = 'I92b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I92b36}')

I92b63 = Parameter(name = 'I92b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I92b63}')

I92b66 = Parameter(name = 'I92b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I92b66}')

I93b11 = Parameter(name = 'I93b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I93b11}')

I93b22 = Parameter(name = 'I93b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I93b22}')

I93b33 = Parameter(name = 'I93b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I93b33}')

I93b36 = Parameter(name = 'I93b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I93b36}')

I94b11 = Parameter(name = 'I94b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                   texname = '\\text{I94b11}')

I94b22 = Parameter(name = 'I94b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                   texname = '\\text{I94b22}')

I94b33 = Parameter(name = 'I94b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I94b33}')

I94b36 = Parameter(name = 'I94b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I94b36}')

I94b63 = Parameter(name = 'I94b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I94b63}')

I94b66 = Parameter(name = 'I94b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I94b66}')

I95b11 = Parameter(name = 'I95b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rn1x1)',
                   texname = '\\text{I95b11}')

I95b22 = Parameter(name = 'I95b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I95b22}')

I95b33 = Parameter(name = 'I95b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I95b33}')

I95b36 = Parameter(name = 'I95b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I95b36}')

I96b11 = Parameter(name = 'I96b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I96b11}')

I96b22 = Parameter(name = 'I96b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I96b22}')

I96b33 = Parameter(name = 'I96b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I96b33}')

I96b36 = Parameter(name = 'I96b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I96b36}')

I96b63 = Parameter(name = 'I96b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I96b63}')

I96b66 = Parameter(name = 'I96b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I96b66}')

I97b11 = Parameter(name = 'I97b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I97b11}')

I97b22 = Parameter(name = 'I97b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I97b22}')

I97b33 = Parameter(name = 'I97b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I97b33}')

I97b36 = Parameter(name = 'I97b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I97b36}')

I97b63 = Parameter(name = 'I97b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I97b63}')

I97b66 = Parameter(name = 'I97b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I97b66}')

I98b11 = Parameter(name = 'I98b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x1*complexconjugate(Ru1x1)',
                   texname = '\\text{I98b11}')

I98b22 = Parameter(name = 'I98b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x2*complexconjugate(Ru2x2)',
                   texname = '\\text{I98b22}')

I98b33 = Parameter(name = 'I98b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I98b33}')

I98b36 = Parameter(name = 'I98b36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I98b36}')

I98b63 = Parameter(name = 'I98b63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I98b63}')

I98b66 = Parameter(name = 'I98b66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I98b66}')

I99b33 = Parameter(name = 'I99b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3',
                   texname = '\\text{I99b33}')

