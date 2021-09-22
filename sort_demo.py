#! -*-encoding:utf-8 -*-
"""
1. 交换排序
    冒泡排序(Bubble Sort)
    快速排序(Quick Sort)

2. 插入排序
    简单插入排序(Insert Sort)
    希尔排序(Shell Sort)

3.选择排序
    简单选择排序(Select Sort)
    堆排序(Heap Sort)

4. 归并排序
    二路归并排序(Two-way Merge Sort)

5. 线性时间非比较类排序
    计数排序（Counting Sort）
    桶排序（Bucket Sort）
    基数排序（Radix Sort）

"""
import random
import copy


def bubble_sort(lst):
    """
        比较相邻的元素。如果第一个比第二个大，就交换它们两个；
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        针对所有的元素重复以上的步骤，除了最后一个；
        重复步骤1~3，直到排序完成。
    """
    target = copy.deepcopy(lst)
    length = len(target)
    if not length:
        return target

    if length == 1:
        return target

    for i in range(length - 1):
        for j in range(length - i - 1):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]

    return target


def quick_sort(lst):
    """
        在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
        数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
        以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。

        举个例子，假设我现在有一个数列需要使用快排来排序：[11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]：
            选取中间的66作为基准值（基准值可以随便选）
            数列从第一个元素11开始和基准值66进行比较，小于基准值，那么将它放入左边的分区中，第二个元素99比基准值66大，把它放入右边的分区中。
            然后依次对左右两个分区进行再分区，直到最后只有一个元素
            分解完成再一层一层返回，返回规则是：左边分区+基准值+右边分区
    """
    target = copy.deepcopy(lst)
    if len(target) < 2:
        return target

    pivot = target[-1]
    target.remove(pivot)
    left = []
    right = []
    for i in target:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


def insert_sort(lst, step=1):
    """
        1. 将待排序列表的第一个元素当做已排序序列，第二个元素到最后一个元素当成未排序序列。
        2. 取未排序序列中的第一个数据，插入到已排序序列中顺序正确的位置。将未排序的第一个数据与相邻的前一个数据(已排序序列的最后一个数)据进行比较，
           如果顺序错误则交换位置，交换位置后继续与相邻的前一个数据进行比较，直到不需要交换则插入完成。每次插入数据后，已排序序列都是排好序的。
        3. 重复上一步，继续插入下一个数据。每进行一次插入，已排序序列的长度加1，未排序序列的长度减1，
           直到列表中的所有数据都插入到已排序序列了，则列表排序完成。
    """
    target = copy.deepcopy(lst)
    length = len(target)
    if length < 2:
        return length

    for i in range(step, length):
        while i - step >= 0:
            if target[i] < target[i - step]:
                target[i - step], target[i] = target[i], target[i - step]
                i -= step
            else:
                break

    return target


def shell_sort(lst):
    """
    希尔排序是小规模数据排序的最优选择，算法的核心思想就是对插入排序的封装，逐渐减小增量形成新的数组进行插入排序。
    最外层循环不断地用数组长度自除以2得到增量increment，直到0为止（不包含0），
    比如N = 64，增量就是[32, 16, 8, 4, 2]内层循环（两层）实现了插入排序，为了防止数组下标溢出，i从increment开始自增，直到N为止（ 不包含N），
    A[i]，A[i - increment], A[i - 2 * increment]...A[i - k * increment]进行排序
    """
    target = copy.deepcopy(lst)
    length = len(target)
    step = length // 2
    while step:
        # for j in range(step, length):  # 3---7
        #     # i 是需要控制的索引
        #     i = j
        #     # 比较的逻辑和控制i的变换的逻辑
        #     while (i - step) >= 0:
        #         if target[i] < target[i - step]:
        #             # 交换
        #             target[i], target[i - step] = target[i - step], target[i]
        #             # 修改i
        #             i -= step
        #         else:
        #             break
        target = insert_sort(target, step=step)
        step = step // 2
    return target


def select_sort(lst):
    """
        工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置
            设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换
            重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序
    """
    target = copy.deepcopy(lst)
    length = len(target)

    for i in range(length-1):
        minIndex = i
        for j in range(i+1, length):
            if target[minIndex] > target[j]:
                minIndex = j
        target[i], target[minIndex] = target[minIndex], target[i]
    return target


if __name__ == "__main__":
    nums = 20
    aList = [random.randint(0, 100) for _ in range(nums)]
    random.shuffle(aList)
    print('{:<15}{}' .format("origin list：", aList))
    print('{:<15}{}'.format("bubble sort：", bubble_sort(aList)))
    print('{:<15}{}'.format("quick sort：", quick_sort(aList)))
    print('{:<15}{}'.format("insert sort：", insert_sort(aList)))
    print('{:<15}{}'.format("shell sort：", shell_sort(aList)))
    print('{:<15}{}'.format("select sort：", select_sort(aList)))

