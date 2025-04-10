<?php

namespace App\Controller\Api;

use App\Dto\PaymentMethodDto;
use App\Entity\PaymentMethod;
use App\Repository\PaymentMethodRepository;
use App\Service\PaymentMethodService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;

#[Route('/api/payment_method')]
final class PaymentMethodController extends AbstractController
{
    public function __construct(
        private PaymentMethodService $paymentMethodService,
        private PaymentMethodRepository $paymentMethodRepository
    ) {}

    #[Route(name: 'api_payment_method_index', methods: ['GET'])]
    public function index(): JsonResponse
    {
        return $this->json($this->paymentMethodRepository->findAll());
    }

    #[Route('/{id}', name: 'api_payment_method_show', methods: ['GET'])]
    public function show(PaymentMethod $paymentMethod): JsonResponse
    {
        return $this->json($paymentMethod);
    }

    #[Route(name: 'api_payment_method_create', methods: ['POST'])]
    public function create(#[MapRequestPayload()] PaymentMethodDto $paymentMethodDto): JsonResponse
    {
        $paymentMethod = $this->paymentMethodService->create($paymentMethodDto);

        return $this->json($paymentMethod, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'api_payment_method_update', methods: ['PUT'])]
    public function update(#[MapRequestPayload()] PaymentMethodDto $paymentMethodDto, PaymentMethod $paymentMethod): JsonResponse
    {
        $updatedPaymentMethod = $this->paymentMethodService->update($paymentMethod, $paymentMethodDto);

        return $this->json($updatedPaymentMethod);
    }

    #[Route('/{id}', name: 'api_payment_method_delete', methods: ['DELETE'])]
    public function delete(PaymentMethod $paymentMethod): JsonResponse
    {
        $this->paymentMethodService->delete($paymentMethod);

        return $this->json(null, Response::HTTP_NO_CONTENT);
    }
}
