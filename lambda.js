{
  const TRUE = (t) => (f) => t();
  const FALSE = (t) => (f) => f();

  const IF = (cond) => (t) => (f) => cond(() => t)(() => f);

  const AND = (a) => (b) => IF(a)(b)(FALSE);

  const OR = (a) => (b) => IF(a)(TRUE)(b);

  console.log(IF(AND(OR(TRUE)(FALSE))(TRUE))(() => 13)(() => 5)()); // => 13
}

{
  const TRUE = (t, f) => t();
  const FALSE = (t, f) => f();

  const IF = (cond) => (t) => (f) => cond(() => t)(() => f);

  const AND = (a) => (b) => IF(a)(b)(FALSE);

  const OR = (a) => (b) => IF(a)(TRUE)(b);

  console.log(IF(AND(OR(TRUE)(FALSE))(TRUE))(() => 13)(() => 5)()); // => 13
}
