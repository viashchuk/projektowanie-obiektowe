<?php

namespace App\Service;

use App\Dto\CategoryDto;
use App\Entity\Category;
use Doctrine\ORM\EntityManagerInterface;

class CategoryService
{
    public function __construct(
        private EntityManagerInterface $entityManager
    ) {}

    public function delete(Category $category): void
    {
        $this->entityManager->remove($category, true);
        $this->entityManager->flush();
    }

    public function create(CategoryDto $categoryDto): Category
    {
        $category = new Category();

        $category->setTitle($categoryDto->title);

        $this->entityManager->persist($category);
        $this->entityManager->flush();

        return $category;
    }

    public function update(Category $category, CategoryDto $categoryDto): Category
    {
        $category->setTitle($categoryDto->title);

        $this->entityManager->persist($category);
        $this->entityManager->flush();

        return $category;
    }
}
