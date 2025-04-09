<?php

namespace App\DataFixtures;

use App\Entity\Product;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        for ($i = 0; $i < 20; $i++) {
            $product = new Product();
            $product->setTitle('product ' . $i);
            $product->setPrice(mt_rand(10, 100));
            $product->setAmount(mt_rand(1, 10));
            $product->setDescription("");

            $manager->persist($product);
        }

        $manager->flush();
    }
}
