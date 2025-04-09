<?php

namespace App\Dto;

use Symfony\Component\Validator\Constraints as Assert;

class ProductDto
{
    public function __construct(
        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $title,

        #[Assert\NotBlank]
        #[Assert\GreaterThan(0)]
        public readonly float $price,

        #[Assert\NotBlank]
        public readonly int $amount,

        #[Assert\Length(max: 1000)]
        public readonly ?string $description = null
    ) {}
}
