# Answer 2
LR: Learning Rate

L: Regularization Parameter

Mom: Momentum(beta)

|     |     LR |   L |   Mom |       Time |     RMSE |      MAE | METHOD                                                           |
|----:|-------:|----:|------:|-----------:|---------:|---------:|:-----------------------------------------------------------------|
|   0 | 0.01   | 0.5 | nan   |  0.0533156 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|   1 | 0.01   | 0.5 | nan   |  0.0477273 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|   2 | 0.01   | 0.5 | nan   |  0.695551  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|   3 | 0.01   | 0.5 | nan   |  0.561059  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|   4 | 0.01   | 0.5 | nan   |  0.431432  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|   5 | 0.01   | 0.5 | nan   | 26.3704    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|   6 | 0.01   | 0.5 | nan   |  0.26541   | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|   7 | 0.01   | 0.5 |   0.1 |  0.0845172 | 0.876565 | 0.71116  | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|   8 | 0.01   | 0.5 | nan   |  0.0423946 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|   9 | 0.01   | 0.5 | nan   |  0.0550349 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|  10 | 0.01   | 0.5 | nan   |  0.198078  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  11 | 0.01   | 0.5 | nan   |  0.290833  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|  12 | 0.01   | 0.5 | nan   |  0.291314  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|  13 | 0.01   | 0.5 | nan   | 24.3749    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  14 | 0.01   | 0.5 | nan   |  0.275993  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  15 | 0.01   | 0.5 |   0.5 |  0.0830278 | 0.876932 | 0.71502  | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  16 | 0.01   | 0.5 | nan   |  0.0470569 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  17 | 0.01   | 0.5 | nan   |  0.0437098 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|  18 | 0.01   | 0.5 | nan   |  0.192425  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  19 | 0.01   | 0.5 | nan   |  0.284148  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|  20 | 0.01   | 0.5 | nan   |  0.285177  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|  21 | 0.01   | 0.5 | nan   | 24.0908    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  22 | 0.01   | 0.5 | nan   |  0.246741  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  23 | 0.01   | 0.5 |   0.9 |  0.0715506 | 0.874455 | 0.710919 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  24 | 0.01   | 0.1 | nan   |  0.0475068 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  25 | 0.01   | 0.1 | nan   |  0.0418236 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
|  26 | 0.01   | 0.1 | nan   |  0.184894  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  27 | 0.01   | 0.1 | nan   |  0.2847    | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
|  28 | 0.01   | 0.1 | nan   |  0.274409  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
|  29 | 0.01   | 0.1 | nan   | 23.7922    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  30 | 0.01   | 0.1 | nan   |  0.246761  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  31 | 0.01   | 0.1 |   0.1 |  0.0710788 | 0.848613 | 0.693309 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  32 | 0.01   | 0.1 | nan   |  0.0419817 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  33 | 0.01   | 0.1 | nan   |  0.0514054 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
|  34 | 0.01   | 0.1 | nan   |  0.188461  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  35 | 0.01   | 0.1 | nan   |  0.270089  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
|  36 | 0.01   | 0.1 | nan   |  0.287206  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
|  37 | 0.01   | 0.1 | nan   | 23.9026    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  38 | 0.01   | 0.1 | nan   |  0.244165  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  39 | 0.01   | 0.1 |   0.5 |  0.0831361 | 0.849874 | 0.697269 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  40 | 0.01   | 0.1 | nan   |  0.0399742 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  41 | 0.01   | 0.1 | nan   |  0.0357835 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
|  42 | 0.01   | 0.1 | nan   |  0.200546  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  43 | 0.01   | 0.1 | nan   |  0.277121  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
|  44 | 0.01   | 0.1 | nan   |  0.278131  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
|  45 | 0.01   | 0.1 | nan   | 24.04      | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  46 | 0.01   | 0.1 | nan   |  0.259065  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  47 | 0.01   | 0.1 |   0.9 |  0.073173  | 0.848371 | 0.691025 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  48 | 0.01   | 1   | nan   |  0.0421619 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  49 | 0.01   | 1   | nan   |  0.0404754 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
|  50 | 0.01   | 1   | nan   |  0.19968   | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  51 | 0.01   | 1   | nan   |  0.303289  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
|  52 | 0.01   | 1   | nan   |  0.291142  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
|  53 | 0.01   | 1   | nan   | 28.4137    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
|  54 | 0.01   | 1   | nan   |  0.349893  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  55 | 0.01   | 1   |   0.1 |  0.0859835 | 0.896566 | 0.7253   | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  56 | 0.01   | 1   | nan   |  0.0403786 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  57 | 0.01   | 1   | nan   |  0.0309193 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
|  58 | 0.01   | 1   | nan   |  0.207975  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  59 | 0.01   | 1   | nan   |  0.319353  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
|  60 | 0.01   | 1   | nan   |  0.292678  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
|  61 | 0.01   | 1   | nan   | 26.4311    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
|  62 | 0.01   | 1   | nan   |  0.255114  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  63 | 0.01   | 1   |   0.5 |  0.0781822 | 0.900139 | 0.727376 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  64 | 0.01   | 1   | nan   |  0.0359168 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  65 | 0.01   | 1   | nan   |  0.0389652 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
|  66 | 0.01   | 1   | nan   |  0.189823  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  67 | 0.01   | 1   | nan   |  0.276342  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
|  68 | 0.01   | 1   | nan   |  0.283364  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
|  69 | 0.01   | 1   | nan   | 24.3725    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
|  70 | 0.01   | 1   | nan   |  0.25262   | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  71 | 0.01   | 1   |   0.9 |  0.080024  | 0.903632 | 0.738705 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  72 | 0.001  | 0.5 | nan   |  0.035552  | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  73 | 0.001  | 0.5 | nan   |  0.0399978 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|  74 | 0.001  | 0.5 | nan   |  0.195902  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  75 | 0.001  | 0.5 | nan   |  0.280915  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|  76 | 0.001  | 0.5 | nan   |  0.281499  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|  77 | 0.001  | 0.5 | nan   | 24.5726    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  78 | 0.001  | 0.5 | nan   |  0.24819   | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  79 | 0.001  | 0.5 |   0.1 |  0.0732853 | 0.878606 | 0.714322 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  80 | 0.001  | 0.5 | nan   |  0.0415711 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  81 | 0.001  | 0.5 | nan   |  0.0364912 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|  82 | 0.001  | 0.5 | nan   |  0.188609  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  83 | 0.001  | 0.5 | nan   |  0.280967  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|  84 | 0.001  | 0.5 | nan   |  0.280889  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|  85 | 0.001  | 0.5 | nan   | 25.0268    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  86 | 0.001  | 0.5 | nan   |  0.251704  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  87 | 0.001  | 0.5 |   0.5 |  0.0712676 | 0.87872  | 0.714224 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  88 | 0.001  | 0.5 | nan   |  0.0387123 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  89 | 0.001  | 0.5 | nan   |  0.0404346 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
|  90 | 0.001  | 0.5 | nan   |  0.191837  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  91 | 0.001  | 0.5 | nan   |  0.310437  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
|  92 | 0.001  | 0.5 | nan   |  0.286593  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
|  93 | 0.001  | 0.5 | nan   | 33.9621    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
|  94 | 0.001  | 0.5 | nan   |  0.333286  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
|  95 | 0.001  | 0.5 |   0.9 |  0.0894618 | 0.878616 | 0.714472 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
|  96 | 0.001  | 0.1 | nan   |  0.0527651 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
|  97 | 0.001  | 0.1 | nan   |  0.0431778 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
|  98 | 0.001  | 0.1 | nan   |  0.256317  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
|  99 | 0.001  | 0.1 | nan   |  0.371505  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 100 | 0.001  | 0.1 | nan   |  0.367914  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 101 | 0.001  | 0.1 | nan   | 33.4956    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 102 | 0.001  | 0.1 | nan   |  0.338861  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 103 | 0.001  | 0.1 |   0.1 |  0.0915306 | 0.848335 | 0.687584 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 104 | 0.001  | 0.1 | nan   |  0.0400805 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 105 | 0.001  | 0.1 | nan   |  0.0386915 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
| 106 | 0.001  | 0.1 | nan   |  0.199035  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 107 | 0.001  | 0.1 | nan   |  0.296871  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 108 | 0.001  | 0.1 | nan   |  0.342025  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 109 | 0.001  | 0.1 | nan   | 27.6739    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 110 | 0.001  | 0.1 | nan   |  0.244664  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 111 | 0.001  | 0.1 |   0.5 |  0.0746245 | 0.848246 | 0.687633 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 112 | 0.001  | 0.1 | nan   |  0.0399444 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 113 | 0.001  | 0.1 | nan   |  0.0430467 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
| 114 | 0.001  | 0.1 | nan   |  0.189895  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 115 | 0.001  | 0.1 | nan   |  0.279002  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 116 | 0.001  | 0.1 | nan   |  0.286485  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 117 | 0.001  | 0.1 | nan   | 24.8938    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 118 | 0.001  | 0.1 | nan   |  0.243177  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 119 | 0.001  | 0.1 |   0.9 |  0.0758023 | 0.848104 | 0.68826  | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 120 | 0.001  | 1   | nan   |  0.0365596 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 121 | 0.001  | 1   | nan   |  0.0315411 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 122 | 0.001  | 1   | nan   |  0.187339  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 123 | 0.001  | 1   | nan   |  0.285092  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 124 | 0.001  | 1   | nan   |  0.30071   | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 125 | 0.001  | 1   | nan   | 28.72      | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 126 | 0.001  | 1   | nan   |  0.324474  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 127 | 0.001  | 1   |   0.1 |  0.0999656 | 0.902024 | 0.730462 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 128 | 0.001  | 1   | nan   |  0.0507371 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 129 | 0.001  | 1   | nan   |  0.0497289 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 130 | 0.001  | 1   | nan   |  0.243068  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 131 | 0.001  | 1   | nan   |  0.369533  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 132 | 0.001  | 1   | nan   |  0.381909  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 133 | 0.001  | 1   | nan   | 30.001     | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 134 | 0.001  | 1   | nan   |  0.260005  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 135 | 0.001  | 1   |   0.5 |  0.0829549 | 0.901853 | 0.730289 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 136 | 0.001  | 1   | nan   |  0.0396214 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 137 | 0.001  | 1   | nan   |  0.0398233 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 138 | 0.001  | 1   | nan   |  0.2044    | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 139 | 0.001  | 1   | nan   |  0.314009  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 140 | 0.001  | 1   | nan   |  0.313217  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 141 | 0.001  | 1   | nan   | 26.1459    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 142 | 0.001  | 1   | nan   |  0.248399  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 143 | 0.001  | 1   |   0.9 |  0.0955729 | 0.901089 | 0.729987 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 144 | 0.0001 | 0.5 | nan   |  0.044452  | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 145 | 0.0001 | 0.5 | nan   |  0.0428619 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
| 146 | 0.0001 | 0.5 | nan   |  0.192103  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 147 | 0.0001 | 0.5 | nan   |  0.289134  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
| 148 | 0.0001 | 0.5 | nan   |  0.283353  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
| 149 | 0.0001 | 0.5 | nan   | 25.8725    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 150 | 0.0001 | 0.5 | nan   |  0.255969  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 151 | 0.0001 | 0.5 |   0.1 |  0.0763164 | 0.90852  | 0.734628 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 152 | 0.0001 | 0.5 | nan   |  0.0403943 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 153 | 0.0001 | 0.5 | nan   |  0.0389948 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
| 154 | 0.0001 | 0.5 | nan   |  0.186936  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 155 | 0.0001 | 0.5 | nan   |  0.30339   | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
| 156 | 0.0001 | 0.5 | nan   |  0.294461  | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
| 157 | 0.0001 | 0.5 | nan   | 25.5757    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 158 | 0.0001 | 0.5 | nan   |  0.264853  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 159 | 0.0001 | 0.5 |   0.5 |  0.072989  | 0.908527 | 0.734624 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 160 | 0.0001 | 0.5 | nan   |  0.0401857 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 161 | 0.0001 | 0.5 | nan   |  0.0384166 | 0.907464 | 0.733933 | Manual and MSE Loss with Ridge Regularization                    |
| 162 | 0.0001 | 0.5 | nan   |  0.204689  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 163 | 0.0001 | 0.5 | nan   |  0.306421  | 0.907464 | 0.733933 | JAX and MSE Loss with Ridge Regularization                       |
| 164 | 0.0001 | 0.5 | nan   |  0.30169   | 0.953716 | 0.765915 | JAX and MSE Loss with LASSO Regularization                       |
| 165 | 0.0001 | 0.5 | nan   | 26.2452    | 0.871825 | 0.713431 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 166 | 0.0001 | 0.5 | nan   |  0.267278  | 0.8598   | 0.698848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 167 | 0.0001 | 0.5 |   0.9 |  0.0918288 | 0.908604 | 0.734634 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 168 | 0.0001 | 0.1 | nan   |  0.0468369 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 169 | 0.0001 | 0.1 | nan   |  0.0362914 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
| 170 | 0.0001 | 0.1 | nan   |  0.234341  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 171 | 0.0001 | 0.1 | nan   |  0.323223  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 172 | 0.0001 | 0.1 | nan   |  0.293689  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 173 | 0.0001 | 0.1 | nan   | 27.5751    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 174 | 0.0001 | 0.1 | nan   |  0.29011   | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 175 | 0.0001 | 0.1 |   0.1 |  0.0831404 | 0.900887 | 0.729573 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 176 | 0.0001 | 0.1 | nan   |  0.0458889 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 177 | 0.0001 | 0.1 | nan   |  0.0398376 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
| 178 | 0.0001 | 0.1 | nan   |  0.204833  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 179 | 0.0001 | 0.1 | nan   |  0.345557  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 180 | 0.0001 | 0.1 | nan   |  0.287568  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 181 | 0.0001 | 0.1 | nan   | 23.997     | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 182 | 0.0001 | 0.1 | nan   |  0.247703  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 183 | 0.0001 | 0.1 |   0.5 |  0.0779102 | 0.90089  | 0.72958  | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 184 | 0.0001 | 0.1 | nan   |  0.0429316 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 185 | 0.0001 | 0.1 | nan   |  0.0451462 | 0.904104 | 0.731729 | Manual and MSE Loss with Ridge Regularization                    |
| 186 | 0.0001 | 0.1 | nan   |  0.200696  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 187 | 0.0001 | 0.1 | nan   |  0.283216  | 0.904104 | 0.731729 | JAX and MSE Loss with Ridge Regularization                       |
| 188 | 0.0001 | 0.1 | nan   |  0.285469  | 0.918442 | 0.742703 | JAX and MSE Loss with LASSO Regularization                       |
| 189 | 0.0001 | 0.1 | nan   | 25.0429    | 0.864605 | 0.710697 | JAX and MSE Loss with Ridge Regularization and SGD               |
| 190 | 0.0001 | 0.1 | nan   |  0.265713  | 0.845414 | 0.686848 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 191 | 0.0001 | 0.1 |   0.9 |  0.0832064 | 0.900993 | 0.729697 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 192 | 0.0001 | 1   | nan   |  0.0431533 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 193 | 0.0001 | 1   | nan   |  0.0406792 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 194 | 0.0001 | 1   | nan   |  0.206825  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 195 | 0.0001 | 1   | nan   |  0.286262  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 196 | 0.0001 | 1   | nan   |  0.308952  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 197 | 0.0001 | 1   | nan   | 25.386     | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 198 | 0.0001 | 1   | nan   |  0.242692  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 199 | 0.0001 | 1   |   0.1 |  0.0768652 | 0.916435 | 0.74002  | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 200 | 0.0001 | 1   | nan   |  0.048177  | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 201 | 0.0001 | 1   | nan   |  0.0495872 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 202 | 0.0001 | 1   | nan   |  0.228556  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 203 | 0.0001 | 1   | nan   |  0.271852  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 204 | 0.0001 | 1   | nan   |  0.279883  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 205 | 0.0001 | 1   | nan   | 25.6865    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 206 | 0.0001 | 1   | nan   |  0.25268   | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 207 | 0.0001 | 1   |   0.5 |  0.080972  | 0.916419 | 0.740007 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |
| 208 | 0.0001 | 1   | nan   |  0.0373614 | 0.903229 | 0.731145 | Manual and Unregularized MSE Loss                                |
| 209 | 0.0001 | 1   | nan   |  0.0390489 | 0.911355 | 0.73647  | Manual and MSE Loss with Ridge Regularization                    |
| 210 | 0.0001 | 1   | nan   |  0.195754  | 0.903229 | 0.731145 | JAX and Unregularized MSE Loss                                   |
| 211 | 0.0001 | 1   | nan   |  0.278361  | 0.911355 | 0.73647  | JAX and MSE Loss with Ridge Regularization                       |
| 212 | 0.0001 | 1   | nan   |  0.282088  | 0.957427 | 0.768181 | JAX and MSE Loss with LASSO Regularization                       |
| 213 | 0.0001 | 1   | nan   | 25.3102    | 0.884382 | 0.72075  | JAX and MSE Loss with Ridge Regularization and SGD               |
| 214 | 0.0001 | 1   | nan   |  0.267508  | 0.877293 | 0.713259 | manual and MSE Loss with Ridge Regularization and minibatch SGD  |
| 215 | 0.0001 | 1   |   0.9 |  0.0828993 | 0.916313 | 0.739916 | JAX and MSE Loss with Ridge Regularization and SGD with momentum |



|Best hyperparameters:|
|---------------------|
|Learning Rate 0.01                      |
|Lamba         0.1                       |
|Momentum      NaN                       |
|Elapsed Time  0.246761                  |
|RMSE          0.845414                  |
|MAE           0.686848                  |
|METHOD        manual and MSE Loss with Ridge Regularisation  |

