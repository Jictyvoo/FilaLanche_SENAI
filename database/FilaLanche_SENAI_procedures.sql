use fila_lanche_senai;
set sql_safe_updates = 0;

delimiter $$
create procedure processar_pedido(in id_produtoCompra int, in id_estudante int, in quantidadeCompra int)
begin
declare quantidade_achada int;
declare busca_quantidade cursor for select quantidade from Produto where id_produto = id_produtoCompra;

open busca_quantidade;
fetch busca_quantidade into quantidade_achada;

update Produto set quantidade = quantidade_achada - quantidadeCompra where id_produto = id_produtoCompra;
insert into Pedido values(id_produtoCompra, id_estudante, now(), quantidadeCompra);
end$$
delimiter ;