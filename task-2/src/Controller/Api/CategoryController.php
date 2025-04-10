<?php

namespace App\Controller\Api;

use App\Dto\CategoryDto;
use App\Entity\Category;
use App\Repository\CategoryRepository;
use App\Service\CategoryService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/api/category')]
final class CategoryController extends AbstractController
{
    public function __construct(
        private CategoryService $categoryService,
        private CategoryRepository $categoryRepository
    ) {}

    #[Route(name: 'api_category_index', methods: ['GET'])]
    public function index(): JsonResponse
    {
        return $this->json($this->categoryRepository->findAll(), 200, [], [
            'groups' => ['category:read']
        ]);
    }

    #[Route('/{id}', name: 'api_category_show', methods: ['GET'])]
    public function show(Category $category): JsonResponse
    {
        return $this->json($category, 200, [], [
            'groups' => ['category:read']
        ]);
    }

    #[Route(name: 'api_category_create', methods: ['POST'])]
    public function create(#[MapRequestPayload()] CategoryDto $categoryDto): JsonResponse
    {
        $category = $this->categoryService->create($categoryDto);

        return $this->json($category, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'api_category_update', methods: ['PUT'])]
    public function update(#[MapRequestPayload()] CategoryDto $categoryDto, Category $category): JsonResponse
    {
        $updatedCategory = $this->categoryService->update($category, $categoryDto);

        return $this->json($updatedCategory, 200, [], [
            'groups' => ['category:read']
        ]);
    }

    #[Route('/{id}', name: 'api_category_delete', methods: ['DELETE'])]
    public function delete(Category $category): JsonResponse
    {
        $this->categoryService->delete($category);

        return $this->json(null, Response::HTTP_NO_CONTENT);
    }
}
