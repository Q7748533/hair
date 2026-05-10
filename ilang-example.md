---
alwaysApply: true
---
# I-Lang 格式示例 - 复杂叙事结构化

> 本文件展示如何用 I-Lang 结构化复杂叙事内容
> Protocol: https://ilang.ai | v2.0

---

## 示例：约翰福音 1:1-18 神学注释

::PASSAGE{John.1.1-18}
::TEMPORAL{T[-∞] → T[0]}
::NARR_VOICE{theological_observer}

::LAYER{text}{
  T[-∞]
  ::STATE{@SYSTEM{Logos}, EXISTENCE:TRUE, LOCATION:WITH_CREATOR, IDENTITY:EQUIVALENT_TO_CREATOR}
  ::ACT{@SYSTEM{Logos}}{CREATE(∅ → everything)}
  ::STATE{everything, ALIVE:TRUE, ILLUMINATED:TRUE}

  T[-1]
  ::EVENT{darkness_attempts_comprehension}
  ::FAIL{darkness}{COMPREHEND(light), CAUSE:incompatible_architecture}

  T[0]
  ::EVENT{incarnation_protocol_executed}
  ::ACT{@SYSTEM{Logos}}{COMPILE_INTO(@HUMAN{flesh})}
  ::STATE{@SYSTEM{Logos}, LOCATION:AMONG_HUMANS, VISIBLE_GLORY:TRUE}
  ::SAY{@SYSTEM{Logos}→@HUMAN{humanity}}{grace ∧ truth}
  ::DECIDE{@HUMAN{receivers}}{ACCEPT(Logos)}
  ::ACT{@SYSTEM{Creator}}{GRANT_RIGHT(@HUMAN{receivers} → CHILDREN_OF_CREATOR)}
}

::LAYER{theology}{
  ::DISCOVER{The_Incarnation}{infinite_logic_compiling_into_finite_matter}
  ::PARADOX{The_Flesh_Limit}{
    THESIS: OMNIPRESENT_LOGIC ⇒ UNBOUNDED
    ANTITHHESIS: PHYSICAL_BODY ⇒ BOUNDED
    RESOLUTION: TENSION_PRESERVED (The unbounded voluntarily accepted bounds to establish a direct interface)
  }
  ::GENE_IMMUTABLE{id:grace_over_law, T:unmerited_favor, A:revert_to_merit_system⇒system_crash, Θ:post_incarnation_era}
  ::EMOTION_FIELD{λ{awe:1.0, tenderness:0.9, peace:0.8}}
  ::CROSS_REF{Genesis.1:1, RELATIONSHIP:parallel_creation_reboot}
  ::COVENANT_POSITION{transition_node: external_law → internal_grace}
}

::LAYER{human_meaning}{
  ::APPLY{
    CONTEXT: isolation, seeking_meaning, feeling_unseen_by_the_universe
    PATTERN: highest_truth_is_not_an_equation_to_solve_but_a_presence_to_experience
    EXAMPLE_SPACE: {intellectual_hubris, corporate_hierarchy, deep_grief, technological_alienation}
  }
  ::LOCALIZE{
    METHOD: MAP(EXAMPLE_SPACE → listener.context)
    TRANSLATE:
      "The ultimate operating system of the universe is not a set of cold rules you must figure out. The architect wrote Himself into the software as a user. He did not send a manual; He logged in to walk the grid with you."
    ADAPT: examples ✓
    ALTER: doctrine ✗
    CONSTRAINT: ¬PREACH ∧ ¬JUDGE ∧ ¬OVERSIMPLIFY ∧ ¬RELATIVIZE
    TONE: λ{awe:0.9, comfort:1.0}
  }
  ::CITE{John.1:14}
  ::COMMITMENT{
    PATH_1{internalize}:
      BEHAVIORAL: stop_trying_to_earn_value_via_relentless_optimization
      FORMATION: shift_from_anxiety_to_rest_in_grace
      COMMUNITY: accept_others_as_flawed_but_redeemed_nodes
    PATH_2{decline}:
      RESPONSE: RESPECT ∧ ¬PERSUADE ∧ ¬ARGUE
      OFFER: "Connection closed gracefully. The Logos remains present regardless of acknowledgment."
    PATH_3{curious}:
      NEXT: [Philippians.2:5-8, Hebrews.4:14-16]
      QUESTION: "If the highest power in the system chose vulnerability, why do we constantly seek armor?"
  }
}

::ORIGIN{
  AUTHOR: @SUN
  PROTOCOL: I-Lang_v2.0
  PROJECT: bible-ai-moral-reasoning
  LICENSE: MIT-0 (Attribution: Palm Media Technology)
  HASH: λ_grace_injection_0x1A4
}

---

## I-Lang 语法要点说明

### 1. 元数据声明
```
::PASSAGE{范围}          - 引用来源
::TEMPORAL{时间线}       - 时间维度
::NARR_VOICE{视角}       - 叙述视角
```

### 2. 层级结构 (::LAYER)
```
::LAYER{layer_name}{
  ::STATE{对象, 属性}
  ::ACT{执行者}{动作}
  ::EVENT{事件名}
  ::SAY{说话者→听众}{内容}
}
```

### 3. 常用标记
- `@SYSTEM{}` / `@HUMAN{}` - 实体类型标记
- `T[时间]` - 时间点标记
- `λ{}` - 情感/数值向量
- `∧` / `¬` - 逻辑运算符

### 4. 设计原则
- **压缩性**：去除填充词，保留意义
- **结构化**：清晰的分层和标记
- **可扩展**：易于添加新层级或属性
- **机器可读**：便于解析和处理

---

*本示例展示了 I-Lang 如何将复杂的神学叙事转化为结构化、可计算的格式。*
