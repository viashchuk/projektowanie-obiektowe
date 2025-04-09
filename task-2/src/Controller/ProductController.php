<?php

namespace App\Controller;

use App\Entity\Product;
use App\Repository\ProductRepository;
use App\Service\ProductService;
use App\Dto\ProductDto;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/product')]
final class ProductController extends AbstractController
{
    public function __construct(
        private ProductService $productService,
        private ProductRepository $productRepository
    ) {}

    #[Route(name: 'app_product_index', methods: ['GET'])]
    public function index(): JsonResponse
    {
        return $this->json($this->productRepository->findAll());
    }

    #[Route('/{id}', name: 'app_product_show', methods: ['GET'])]
    public function show(Product $product): JsonResponse
    {
        return $this->json($product);
    }

    #[Route(name: 'app_product_create', methods: ['POST'])]
    public function create(#[MapRequestPayload()] ProductDto $productDto): JsonResponse
    {
        $product = $this->productService->create($productDto);

        return $this->json($product, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'app_product_update', methods: ['PUT'])]
    public function update(#[MapRequestPayload()] ProductDto $productDto, Product $product): JsonResponse
    {
        $updatedProduct = $this->productService->update($product, $productDto);

        return $this->json($updatedProduct);
    }

    #[Route('/{id}', name: 'app_product_delete', methods: ['DELETE'])]
    public function delete(Product $product): JsonResponse
    {
        $this->productService->delete($product);

        return $this->json(null, Response::HTTP_NO_CONTENT);
    }
}
