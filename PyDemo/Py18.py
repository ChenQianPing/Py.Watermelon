# 折线图
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# mpl.rcParams['legend.fontsize'] = 10
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z ** 2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
#
# plt.show()

# 散点图
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def randrange(n, vmin, vmax):
#     '''
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     '''
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# n = 100
#
# # For each set of style and range settings, plot n random points in the box
# # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()

# 线框图
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.05)
#
# # Plot a basic wireframe.
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#
# plt.show()

# 表面图
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# Z = np.sin(R)
#
# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()

# 箭头图
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Make the grid
# x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
#                       np.arange(-0.8, 1, 0.2),
#                       np.arange(-0.8, 1, 0.8))
#
# # Make the direction data for the arrows
# u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
# v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
# w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
#      np.sin(np.pi * z))
#
# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
#
# plt.show()

# 2D转3D图
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Plot a sin curve using the x and y axes.
# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')
#
# # Plot scatterplot data (20 2D points per colour) on the x and z axes.
# colors = ('r', 'g', 'b', 'k')
# x = np.random.sample(20 * len(colors))
# y = np.random.sample(20 * len(colors))
# labels = np.random.randint(3, size=80)
#
# # By using zdir='y', the y value of these points is fixed to the zs value 0
# # and the (x,y) points are plotted on the x and z axes.
# ax.scatter(x, y, zs=0, zdir='y', c=labels, label='points in (x,z)')
#
# # Make legend, set axes limits and labels
# ax.legend()
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # Customize the view angle so it's easier to see that the scatter points lie
# # on the plane y=0
# ax.view_init(elev=20., azim=-35)
#
# plt.show()

# 文本图
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Demo 1: zdir
# zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
# xs = (1, 4, 4, 9, 4, 1)
# ys = (2, 5, 8, 10, 1, 2)
# zs = (10, 3, 8, 9, 1, 8)
#
# for zdir, x, y, z in zip(zdirs, xs, ys, zs):
#     label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
#     ax.text(x, y, z, label, zdir)
#
# # Demo 2: color
# ax.text(9, 0, 0, "red", color='red')
#
# # Demo 3: text2D
# # Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
# ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
#
# # Tweaking display region and labels
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.set_zlim(0, 10)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
#
# plt.show()

# 3D拼图
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
# from matplotlib import cm
# import numpy as np
#
# # set up a figure twice as wide as it is tall
# fig = plt.figure(figsize=plt.figaspect(0.5))
#
# # ===============
# #  First subplot
# # ===============
# # set up the axes for the first plot
# ax = fig.add_subplot(1, 2, 1, projection='3d')
#
# # plot a 3D surface like in the example mplot3d/surface3d_demo
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf, shrink=0.5, aspect=10)
#
# # ===============
# # Second subplot
# # ===============
# # set up the axes for the second plot
# ax = fig.add_subplot(1, 2, 2, projection='3d')
#
# # plot a 3D wireframe like in the example mplot3d/wire3d_demo
# X, Y, Z = get_test_data(0.05)
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#
# plt.show()

# 雷达图
# import numpy as np
# import matplotlib.pyplot as plt
#
# #标签
# labels = np.array(['智力','战斗力','敏捷度','身高','饭量','体重','酒量'])
# #数据个数
# dataLenth = 7
# #数据
# data = np.array([8,9,5,8,9,9,10])
#
# angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
# data = np.concatenate((data, [data[0]])) # 闭合 # #将数据结合起来
# angles = np.concatenate((angles, [angles[0]])) # 闭合
#
# fig = plt.figure()
# ax = fig.add_subplot(121, polar=True)# polar参数！！代表画圆形！！！！
# #111代表总行数总列数位置
# ax.plot(angles, data, 'bo-', linewidth=1)# 画线四个参数为x,y,标记和颜色，闲的宽度
# ax.fill(angles, data, facecolor='r', alpha=0.1)# 填充颜色和透明度
# ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
# ax.set_title("老齐属性分析", va='baseline', fontproperties="SimHei")
# ax.set_rlim(0,10)
# ax.grid(True)
# plt.show()




