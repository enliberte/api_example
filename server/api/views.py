from django.shortcuts import render
from django.http import HttpResponse


def SumAPI(request, args):
    nums = list(map(lambda x: int(x), args.strip('()').split(',')))
    return HttpResponse("%s" % sum(nums))


def DiffAPI(request, args):
    nums = list(map(lambda x: int(x), args.strip('()').split(',')))
    diff = nums[0]
    for index in range(1, len(nums)):
        diff -= nums[index]
    return HttpResponse("%s" % diff)
