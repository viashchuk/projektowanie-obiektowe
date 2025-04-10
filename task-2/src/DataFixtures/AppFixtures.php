<?php

namespace App\DataFixtures;

use App\Entity\Category;
use App\Entity\PaymentMethod;
use App\Entity\Product;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {

        $categories = [];

        for ($i = 0; $i < 20; $i++) {
            $category = new Category();
            $category->setTitle('category ' . $i);

            $manager->persist($category);
            $categories[] = $category;
        }

        $paymentMethods = [
            ['code' => 'card', 'title' => 'Credit Card'],
            ['code' => 'paypal', 'title' => 'PayPal'],
            ['code' => 'apple', 'title' => 'Apple Pay'],
        ];

        foreach ($paymentMethods as $i => $data) {
            $method = new PaymentMethod();
            $method->setCode($data['code']);
            $method->setTitle($data['title']);
            $method->setActive(true);

            $manager->persist($method);
        }

        for ($i = 0; $i < 20; $i++) {
            $product = new Product();
            $product->setTitle('product ' . $i);
            $product->setPrice(mt_rand(10, 100));
            $product->setAmount(mt_rand(1, 10));
            $product->setDescription("");


            $randomCategory = $categories[array_rand($categories)];
            $product->setCategory($randomCategory);

            $manager->persist($product);
        }

        $manager->flush();
    }
}