<?php

namespace App\DataFixtures;

use App\Entity\Category;
use App\Entity\PaymentMethod;
use App\Entity\Product;
use App\Entity\User;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;
use Symfony\Component\PasswordHasher\Hasher\UserPasswordHasherInterface;

class AppFixtures extends Fixture
{
    public function __construct(
        private UserPasswordHasherInterface $passwordHasher
    ) {}

    public function load(ObjectManager $manager): void
    {
        $user = new User();
        $user->setEmail('admin@test.com');

        $hashedPassword = $this->passwordHasher->hashPassword($user, 'admin');
        $user->setPassword($hashedPassword);

        $user->setRoles(['ROLE_ADMIN']);

        $manager->persist($user);

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