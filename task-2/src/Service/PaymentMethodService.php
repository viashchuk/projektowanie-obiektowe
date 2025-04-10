<?php

namespace App\Service;

use App\Dto\PaymentMethodDto;
use App\Entity\PaymentMethod;
use Doctrine\ORM\EntityManagerInterface;

class PaymentMethodService
{
    public function __construct(
        private EntityManagerInterface $entityManager
    ) {}

    public function delete(PaymentMethod $paymentMethod): void
    {
        $this->entityManager->remove($paymentMethod, true);
        $this->entityManager->flush();
    }

    public function create(PaymentMethodDto $paymentMethodDto): PaymentMethod
    {
        $paymentMethod = new PaymentMethod();

        $paymentMethod->setTitle($paymentMethodDto->title);

        $this->entityManager->persist($paymentMethod);
        $this->entityManager->flush();

        return $paymentMethod;
    }

    public function update(PaymentMethod $paymentMethod, PaymentMethodDto $paymentMethodDto): PaymentMethod
    {
        $paymentMethod->setTitle($paymentMethodDto->title);

        $this->entityManager->persist($paymentMethod);
        $this->entityManager->flush();

        return $paymentMethod;
    }
}
