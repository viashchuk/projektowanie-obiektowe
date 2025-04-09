<?php

namespace App\Service;

use App\Dto\ProductDto;
use App\Entity\Product;
use Doctrine\ORM\EntityManagerInterface;

class ProductService
{
    public function __construct(
        private EntityManagerInterface $entityManager
    ) {}

    public function delete(Product $product): void
    {
        $this->entityManager->remove($product, true);
        $this->entityManager->flush();
    }

    public function create(ProductDto $productDto): Product
    {
        $product = new Product();

        $product->setTitle($productDto->title);
        $product->setPrice($productDto->price);
        $product->setAmount($productDto->amount);
        $product->setDescription($productDto->description);

        $this->entityManager->persist($product);
        $this->entityManager->flush();

        return $product;
    }

    public function update(Product $product, ProductDto $productDto): Product
    {
        $product->setTitle($productDto->title);
        $product->setPrice($productDto->price);
        $product->setAmount($productDto->amount);
        $product->setDescription($productDto->description);

        $this->entityManager->persist($product);
        $this->entityManager->flush();

        return $product;
    }
}
