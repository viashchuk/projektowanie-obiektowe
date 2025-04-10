<?php

namespace App\Dto;

use Symfony\Component\Validator\Constraints as Assert;

class PaymentMethodDto
{
    public function __construct(
        #[Assert\NotBlank]
        public readonly string $code,

        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $title,

        #[Assert\Type('bool')]
        public readonly bool $active,
    ) {}
}
