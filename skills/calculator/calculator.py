#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Calculator:
    def __init__(self, config):
        self.language = config["language"]["calculator"]
        return

    def addition(self, first, second):
        return self.language["addition"].format(
            first, second, self.num_to_words(first + second)
        )

    def subtraction(self, first, second):
        return self.language["subtraction"].format(
            first, second, self.num_to_words(first - second)
        )


    def multiplication(self, first, second):
        return self.language["multiplication"].format(
            first, second, self.num_to_words(first * second)
        )

    def division(self, first, second):
        if second == 0:
            return self.language["division_impossible"]
        return  self.language["division"].format(
            first, second, self.num_to_words(first / second)
        )

    def root(self, first):
        return self.language["root"].format(
            first, self.num_to_words(math.sqrt(first))
        )


    def num_to_words(self, num):
        if isinstance(num, float):
            if num % 1 == 0:
                words = str(int(num))
            else:
                pre, post = str(num).split('.')
                words = self.language["comma_or_point"].format(pre, post)
        else:
            words = str(num)
        return words




