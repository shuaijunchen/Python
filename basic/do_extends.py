#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print 'Dog is running...'

	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	def run(self):
		print 'Cat is running...'

class Tortoise(Animal):
	def run(self):
		print 'Tortoise is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print isinstance(dog, Animal)
print isinstance(cat, Animal)

a = list()
print isinstance(a, Animal)

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())