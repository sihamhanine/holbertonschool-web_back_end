export default function getListStudentIds(array1) {
  const newArray1 = [];
  if (array1 instanceof Array) {
    return array1.map((item) => item.id);
  }
  return newArray1;
}
